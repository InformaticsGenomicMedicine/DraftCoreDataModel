import re 
import json
class CoreVariantClass:

    """ The CoreVariantClass is draft schema."""

    def __init__(self, origCoordSystem, seqType: str, refAllele: str,
                 altAllele: str, start: int, end: int, allelicState: str = None,
                 geneSymbol: str = None, hgncId: int = None, chrom: str = None,
                 genomeBuild: str = None, sequenceId: str = None, **kwargs):
        
        # saving initial parameters
        self.initParamValues = {'origCoordSystem':origCoordSystem,
                                'seqType':seqType,
                                'refAllele':refAllele,
                                'altAllele':altAllele,
                                'start':start,'end':end,
                                'allelicState':allelicState,
                                'geneSymbol':geneSymbol, 
                                'hgncId':hgncId,
                                'chrom':chrom, 
                                'genomeBuild':genomeBuild, 
                                'sequenceId':sequenceId,
                                'extra':kwargs }

        # saving validating parameters
        self._validate_input(chrom,genomeBuild,sequenceId)
        self.origCoordSystem = self._validate_orig_coord_system(origCoordSystem)
        self.seqType = self._validate_seq_type(seqType)
        self.refAllele = self._validate_reference_allele(refAllele,'refAllele')
        self.altAllele = self._validate_alternative_allele(altAllele,'altAllele')
        self.start = self._validate_coordinates(start,'start')
        self.end =  self._validate_coordinates(end,'end')
        self._validate_start_coord_end_coord()
        self.allelicState = self._is_valid_allelic_state(allelicState)
        self.geneSymbol = self._is_valid_gene_symbol(geneSymbol)
        self.hgncId = self._is_valid_hgnc_id(hgncId)
        self.chrom = self._validate_chrom(chrom)
        self.genomeBuild = self._validate_genome_build(genomeBuild)
        self.sequenceId = self._validate_sequence_id(sequenceId)
        self.extra = kwargs

    def __repr__(self):
        """Returns a string representation of the CoreVariantClass object.

        Returns:
            str: A string representation of the CoreVariantClass object.
        """
        return f"CoreVariantClass({self.origCoordSystem},{self.seqType},{self.refAllele},{self.altAllele},{self.start},{self.end},{self.allelicState},{self.geneSymbol},{self.hgncId},{self.chrom},{self.genomeBuild},{self.sequenceId},{self.extra})"

    def as_dict(self):
        """Converts CoreVariantClass object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object 
        """
        return {'origCoordSystem':self.origCoordSystem,'seqType':self.seqType,
                'refAllele':self.refAllele,'altAllele':self.altAllele,
                'start':self.start,'end':self.end,'allelicState':self.allelicState,
                'geneSymbol':self.geneSymbol,'hgncId':self.hgncId,'chrom':self.chrom,
                'genomeBuild':self.genomeBuild,'sequenceId':self.sequenceId,'extra':self.extra}

    def as_json(self):
        """Converts CoreVariantClass object to a JSON string representation. 

        Returns:
            str: A JSON formatted string of the CoreVariantClass object.
        """
        return json.dumps(self.as_dict()) 
    
    def init_params(self):
        """ A dictionary of the initial parameters. 

        Returns:
            dict: A dictionary (Key: Initial parameters, Values: parameters values). 
        """
        return self.initParamValues

    def normalized_data(self):
        """A dictionary of the normalized data. This method checks to see if the initial parameters can be normalized and validated. 

        Raises:
            ValueError: If the origCoordSystem is not "0-based interbase".

        Returns:
            dict: A dictionary of the normalized data with validate attribute values. 
        """
        if self.initParamValues['origCoordSystem'] == "0-based interbase":
            return {
            'origCoordSystem': self.origCoordSystem,
            'seqType':  self.seqType,
            'allelicState': self.allelicState,
            'associatedGene': {'geneSymbol':self.geneSymbol,'hgncId':self.hgncId},
            'refAllele': self.refAllele,
            'altAllele': self.altAllele,        
            'position': {
                'chrom':self.chrom,
                'genomeBuild':self.genomeBuild,
                'start':self.start,
                'end':self.end,
                'sequenceId':self.sequenceId}
                }
        else:
            raise ValueError('Data can not be normalized, origCoordSystem is not "0-based interbase".')
        
    #TODO: think of a better method name
    def _validate_input(self,chrom,genomeBuild,sequenceId):
        """_summary_

        Args:
            chrom (str): _description_
            genomeBuild (str): _description_
            sequenceId (str): _description_

        Raises:
            ValueError: _description_
        """
        if not ((chrom and genomeBuild) or sequenceId):
            raise ValueError("Required to have both (chrom AND genomeBuild) or sequenceId")   
              
    def _validate_orig_coord_system(self,origCoordSystem):
        """ Validate origCoordSystem input. Method checks if the provided origCoordSystem
        is one of the allowed types: ('0-based interbase','0-based counting','1-based counting').

        Args:
            coordSystem (str): The origCoordSystem to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str: One of the allowed types. 
        """
        value = origCoordSystem.strip()
        allowedOrigCoordSystem = ('0-based interbase','0-based counting','1-based counting')
        if value not in allowedOrigCoordSystem:
            raise ValueError(f'Invalid origCoordSystem input: "{origCoordSystem}". Allowed types: {allowedOrigCoordSystem}.')
        return value

    def _validate_seq_type(self,seqType):
        """ Validate seqType input. Method checks if the provided seqType is one of the allowed types: ('DNA','RNA','PROTEIN'). 

        Args:
            seqType (str): The seqType to be validated. 

        Raises:
            ValueError: If the provided input is not one of the allowed types. 

        Returns:
            str: One of the allowed types in uppercase. 
        """
        value = seqType.upper().strip()
        allowedSeqType = ('DNA','RNA','PROTEIN')
        if value not in allowedSeqType:
            raise ValueError(f'Invalid seqType input: "{seqType}". Allowed types: {allowedSeqType} (Case Insensitive).') 
        return value

    # TODO: Edit doc strings
    def _validate_reference_allele(self,value,attributeName):
        """ Validate the refAllele input. Method checks if input value matches regular expression pattern (^[a-zA-Z0-9\s]*$).
        
        Args:
            value (str): The reference or alternative allele to be validated.
            attributeName (str): The name of the attribute that is being validated. Used for the error message.

        Raises:
            ValueError: If the provided value does not match regular expression pattern. 

        Returns:
            str: The validated reference or alternative allele input.
        """
        val = value.upper().strip()

        pat = {
            'emp_pat':'^$',
            'digit':r'^\d+$',
            'DNA':r'^[ACGT]*$',
            'RNA':r'^[ACGU]*$',
            'PROTEIN':r'^[ACDEFGHIKLMNPQRSTVWY]*$'
        }
        
        if re.match(pat['emp_pat'],val,re.IGNORECASE):
            return '' 
        
        if self.seqType in ('DNA', 'RNA'):
            if not (re.match(pat[self.seqType], val) or re.match(pat['digit'], val)):
                raise ValueError(f'Invalid {attributeName} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]} or {pat["digit"]}).')
            return val
        elif self.seqType == 'PROTEIN':
            if not re.match(pat['PROTEIN'],val):
                raise ValueError(f'Invalid {attributeName} input: "{val}". Value need to match regular expression patter: ({pat["PROTEIN"]}).')
            return val

    # TODO: Edit doc strings 
    def _validate_alternative_allele(self,value,attributeName):
        """ Validate the altAllele input. Method checks if input value matches regular expression pattern (^[a-zA-Z0-9\s]*$).
        
        Args:
            value (str): The reference or alternative allele to be validated.
            attributeName (str): The name of the attribute that is being validated. Used for the error message.

        Raises:
            ValueError: If the provided value does not match regular expression pattern. 

        Returns:
            str: The validated reference or alternative allele input.
        """
        val = value.upper().strip()

        pat = {
            'emp_pat': '^$',
            'DNA':r'^[ACGT]*$',
            'RNA':r'^[ACGU]*$)',
            'PROTEIN':r'^[ACDEFGHIKLMNPQRSTVWY]*$'
        }

        if re.match(pat['emp_pat'],value,re.IGNORECASE):
            return '' 
        if self.seqType in ('DNA','RNA'):
            if not re.match(pat[self.seqType]):
                raise ValueError(f'Invalid {attributeName} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]}).')
        elif self.seqType == 'PROTEIN':
            if not re.match(pat['PROTEIN']):
                raise ValueError(f'Invalid {attributeName} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]}).')
        
    def _validate_coordinates(self, value, attributeName):
        """ Validate the coordinate input. Method checks if the value is an integer and is greater than or equal to 0.

        Args:
            value (int): The coordinate value to be validated. 
            attributeName (str): The name of the attribute that is being validated. Used for the error message.

        Raises:
            ValueError: If the provided input is not an integer or less than 0. 

        Returns:
            int: The validated coordinate value. 
        """
        if not isinstance(value,int):
            raise ValueError(f'Invalid {attributeName} input: "{value}": is not an integer.')
        if value < 0:
            raise ValueError(f'Invalid {attributeName} input: "{value}": is not greater then or equal to 0.')
        return value

    def _validate_start_coord_end_coord(self):
        """ Validate the start and end coordinate input. Method checks if the start coordinate is grater than or equal to the 
        end coordinate. 

        Raises:
            ValueError: If the start coordinate is greater than or equal to the end coordinate. 
        """
        if self.start >= self.end:
            raise ValueError(f"The start coordinate value: {self.start} can not be greater than or equal to the end coordinate value {self.end}.")

    def _is_valid_allelic_state(self,allelicState):
        """Validate allelicState input. Method checks if the provided allelicState is one of the allowed types: ('heterozygous','homozygous').

        Args:
            allelicState (str): The allelicState to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str: One of the allowed types in lowercase.
        """
        if allelicState is None:
            return allelicState
        
        value = allelicState.lower().strip()
        allowed_allelicState = ('heterozygous','homozygous')
        if value not in allowed_allelicState:
            raise ValueError(f'Invalid allelicState input: "{allelicState}". Allowed types: {allowed_allelicState} (Case Insensitive).')
        return value

    def _is_valid_gene_symbol(self,geneSymbol):
        """Validate geneSymbol input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9]*$ .

        Args:
            geneSymbol (str): The geneSymbol to be validated.

        Raises:
            ValueError: If the provided input does not match regular expression pattern. 

        Returns:
            str: The validated geneSymbol value input. 
        """
        if geneSymbol is None:
            return geneSymbol
        
        pat = r'^[a-zA-Z0-9]*$'
        value = geneSymbol.strip()
        if not re.match(pat,value):
            raise ValueError(f'Invalid geneSymbol input: "{geneSymbol}". Allowed type: alphanumeric characters only.')
        return value

    def _is_valid_hgnc_id(self,hgncId):
        """ Validate the hgncId input. Method checks if the value is an integer and is greater than 1.

        Args:
            hgncId (int): The hgncId value to be validated. 

        Raises:
            ValueError: If the provided input is not an integer or less than 1. 

        Returns:
            int:  The validated hgncId value input. 
        """
        if hgncId is None:
            return hgncId

        if not isinstance(hgncId,int):
            raise ValueError(f'Invalid hgncId input: "{hgncId}": is not an integer.')
        if hgncId < 1:
            raise ValueError(f'Invalid hgncId input: "{hgncId}": is not greater then or equal to 1.')
        return hgncId

    def _validate_chrom(self,chrom):
        """ Validate chrom input. Method checks if the provided chromosome is one of the allowed inputs: (1-22, X, Y, MT) or None.

        Args:
            chrom (str or None): The chrom to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str or None: One of the allowed types. 
        """

        if chrom is None:
            return chrom
        
        value = chrom.upper().strip()

        allowedChrom = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
                     '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'MT')
        
        pat = r'^(chr\s*)?([0-9a-zA-z]+)$'

        match = re.match(pat,value,re.IGNORECASE)

        if not match:
            raise ValueError(f'Invalid chrom input: "{chrom}". It does not match the expected format.')
        
        chromValue = match.group(2)
        if chromValue not in allowedChrom:
            raise ValueError(f'Invalid chrom input:"{chrom}". Allowed types: {allowedChrom}')
        return chromValue
    
    # TODO: Edit doc strings 
    def _validate_genome_build(self,genomeBuild):
        """ Validate genomeBuild input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9]*$ or None.

        Args:
            genomeBuild (str or None): The genomeBuild to be validated.

        Raises:
            ValueError: If the provided input does not match regular expression pattern. 

        Returns:
            str or None: The validated genomeBuild value input. 
        """
        # pat = r'^[a-zA-Z0-9]*$'
        
        if genomeBuild is None:
            return genomeBuild
        value = genomeBuild.strip()
        if not isinstance(value,str):
            raise ValueError(f'Invalid genomeBuild input: "{genomeBuild}". ALlowed types: None or string')
        return value
    
    def _validate_sequence_id(self,sequenceId):
        """ Validate sequenceId input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9_.]+$ or None.

        Args:
            sequenceId (str or None): The sequenceId to be validated.

        Raises:
            ValueError: If the provided input does not match regular expression pattern. 

        Returns:
            str or None: The validated sequenceId value input. 
        """
        # need to modify this regular expression to allow . and _: Example: NC_000004.11
        pat = r'^[a-zA-Z0-9_.]+$'
        if sequenceId is None:
            return sequenceId
        value = sequenceId.strip()
        if not re.match(pat,value):
            raise ValueError(f'Invalid sequenceId input: "{sequenceId}".ALlowed types: alphanumeric characters only.')
        return value