# Citation: https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/extras/translator.py
# Citation: https://github.com/biocommons/hgvs


import re

from src.spdi.spdi_utils import SPDITranslate
from src.core_variant import CoreVariantClass
from src.api.seqrepo_api import SeqRepoAPI
from src.spdi.spdi_class import SPDI

import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator

class CVCTranslator:
    """Variation (HGVS,SPDI,VRS) to CoreVariantClass Translator"""
    def __init__(self):
        self.trans_spdi = SPDITranslate()
        self.hp = hgvs.parser.Parser()
        self.seqrepo_api = SeqRepoAPI()
        self.dp = self.seqrepo_api.seqrepo_data_proxy 
        self.hdp = hgvs.dataproviders.uta.connect()
        self.vr = hgvs.validator.Validator(hdp=self.hdp)
        # self.spdi = SPDI()

    def _detect_sequence_type(self, input_str):
        """ Detects that sequence type based on the reference sequence provided.
        Formatted reference sequence: 
            * NC_, NM_, NG_, NR_, NP_

        Args:
            input_str (str): A string representing the reference sequence.

        Raises:
            ValueError: If the input reference sequence is not one of the following format: NC_, NM_, NG_, NR_, NP_

        Returns:
            str: The sequence type which can be "DNA", "RNA", or "protein".
        """
        sequence_prefix_map = {
            "NC_": "DNA",
            "NM_": "DNA",
            "NG_": "DNA",
            "NR_": "RNA",
            "NP_": "protein",
        }
        sequence_prefix = input_str.split(":")[0][:3]

        sequence_type = sequence_prefix_map.get(sequence_prefix)

        if sequence_type is None:
            raise ValueError("Unknown sequence type")

        return sequence_type
    
    def spdi_to_cvc(self, expression):
        """Converts an SPDI expression to a CoreVariantClass object.

        Args:
            expression (str): An SPDI expression. 

        Raises:
            ValueError: If the provided SPDI expression is invalid.

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        # extract the 4 attributes from the spdi expression to create a new spdi object with validation method
        s, p, d, i = expression.split(":")
        spdi = SPDI(sequence=s, position=p, deletion=d, insertion=i)
        
        # capture the deletion length from the spdi expression.
        if isinstance(spdi.deletion, int):
            del_len = spdi.deletion
        else:
            del_len = len(str(spdi.deletion)) 

        start_pos = int(spdi.position)
        end_pos = start_pos + del_len

        # Create a CoreVariantClass object from the spdi expression
        try:
            return CoreVariantClass(
                origCoordSystem="0-based interbase",
                seqType=self._detect_sequence_type(expression),
                refAllele=spdi.deletion,  
                altAllele=spdi.insertion,  
                start=start_pos,
                end=end_pos,
                sequenceId=spdi.sequence
                # kwargs= expression
            )
        except Exception as e:
            raise ValueError(
                f"Error creating CoreVariantClass from SPDI: {e}. SPDI Expression: {expression}"
            )

    def hgvs_to_cvc(self, expression):
        """Converts an HGVS expression to a CoreVariantClass object.
            Only supports (ins,sub,del,delins,or dup) HGVS expressions.

        Args:
            expression (str): An HGVS expression. 

        Raises:
            ValueError: If the HGVS expression is in the intronic region
            ValueError: if the HGVS expression is not a supported type. 

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        # validate hgvs input
        parsed_variant = self.hp.parse_hgvs_variant(expression)
        if not self.vr.validate(parsed_variant):
            raise(ValueError(f"Invalid HGVS expression: {expression}"))

        # checks if posedit.pos is an intronic region
        if isinstance(parsed_variant.posedit.pos, hgvs.location.BaseOffsetInterval):
            # checks if the start or end position is intronic
            if (parsed_variant.posedit.pos.start.is_intronic or parsed_variant.posedit.pos.end.is_intronic):
                raise ValueError(f"Intronic HGVS variants are not supported ({parsed_variant.posedit})")
        
        # Generating start and end positions based on the HGVS expression
        # Generating reference and alternative alleles based on the HGVS expression

        if parsed_variant.posedit.edit.type == "ins":
            start_pos = parsed_variant.posedit.pos.start.base
            # end position needs to be the same as the start position for insertions
            end_pos = parsed_variant.posedit.pos.start.base

            ref_seq = parsed_variant.posedit.edit.ref or ""
            alt_seq = parsed_variant.posedit.edit.alt

        elif parsed_variant.posedit.edit.type in ("sub","del","delins","identity","dup"):
            # The starting position is changed to account for 0-interbase indexing
            start_pos = parsed_variant.posedit.pos.start.base - 1 
            end_pos = parsed_variant.posedit.pos.end.base

            if parsed_variant.posedit.edit.type == "sub":
                ref_seq = parsed_variant.posedit.edit.ref
                alt_seq = parsed_variant.posedit.edit.alt

            elif parsed_variant.posedit.edit.type == "del":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = parsed_variant.posedit.edit.alt or ""
                
            elif parsed_variant.posedit.edit.type == "delins":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = parsed_variant.posedit.edit.alt
            
            elif parsed_variant.posedit.edit.type == "identity":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                if not ref_seq:
                    ref_seq = parsed_variant.posedit.edit.alt or ""
                alt_seq = ref_seq

            elif parsed_variant.posedit.edit.type == "dup":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = ref_seq + ref_seq
        else:
            raise ValueError(
                f"HGVS variant type {parsed_variant.posedit.edit.type} is unsupported"
            )

        # Create a CoreVariantClass object from the HGVS expression
        cvc_instance = CoreVariantClass(
            origCoordSystem="0-based interbase",
            seqType=self._detect_sequence_type(expression),
            refAllele= ref_seq, 
            altAllele= alt_seq, 
            start=start_pos,
            end=end_pos,
            sequenceId=parsed_variant.ac,
            # kwargs=expression
        )

        return cvc_instance
    
    def vrs_to_cvc(self, expression):
        """Converts an VRS expression to a CoreVariantClass object.

        Args:
            expression (str): An VRS expression.

        Raises:
            ValueError: If there is an issue translating the sequence id using the SeqRepoRESTDataProxy.

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        sequence_id = str(expression.location.sequence_id)

        translated_sequence_ids = self.dp.translate_sequence_identifier(
            # we are specifying we only want the reference sequence id. 
            sequence_id, namespace="refseq"
        )
        if not translated_sequence_ids:
            raise ValueError(f"Unable to translate VRS Sequence ID: {sequence_id}")
        

        #translated_sequence_id returns example format: 'refseq:NC_000019.10'
        # we want to extract the sequence id from the translated_sequence_id
        ref_sequence_id_parts = translated_sequence_ids[0].split(":")
        if len(ref_sequence_id_parts) < 2:
            raise ValueError(f"Invalid translated sequence identifier format: {translated_sequence_ids[0]}")
        
        ref_sequence_id = ref_sequence_id_parts[1]

        # Capture the reference sequence
        ref_seq = str(
            self.dp.get_sequence(
                ref_sequence_id, 
                expression.location.interval.start.value, 
                expression.location.interval.end.value,
                )
            )

        # reference: look into this: https://github.com/ga4gh/vrs-python/blob/593508c6e8229336ca1f53a06f69966020cd68f7/src/ga4gh/vrs/extras/translator.py#L412
        # Capture the alternative sequence
        if expression.state.sequence:
            alt_seq = str(expression.state.sequence)
        else:
            alt_seq = "" #None

        start_pos = int(expression.location.interval.start.value)
        end_pos = int(expression.location.interval.end.value)
        
        # Creating a CoreVariantClass object from the VRS expression
        return CoreVariantClass(
            origCoordSystem="0-based interbase",
            seqType=self._detect_sequence_type(ref_sequence_id),
            refAllele=ref_seq,
            altAllele=alt_seq,
            start=start_pos,
            end=end_pos,
            sequenceId=ref_sequence_id,
            # kwargs=expression
        )
