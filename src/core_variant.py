import re 

class CoreVariantClass:
    
    """This Class is used to create a CoreVariantClass object. It contains methods (initParams and normalizedData) and validation methods for every parameter."""

    def __init__(self,origCoordSystem,seqType:str,refAllele:str,
                  altAllele:str, start:int, end:int, allelicState:str,
                  geneSymbol:str, hgncId:int, chrom=None, genomeBuild=None, sequenceId=None):
        
        self.origCoordSystem = self._validate_origCoordSystem(origCoordSystem)
        self.seqType = seqType
        self.refAllele = refAllele
        self.altAllele = altAllele
        self.start = start
        self.end =  end
        self.allelicState = allelicState
        self.geneSymbol = geneSymbol
        self.hgncId = hgncId
        self.chrom = chrom
        self.genomeBuild = genomeBuild
        self.sequenceId = sequenceId

        if not ((chrom and genomeBuild) or sequenceId):
            raise ValueError("Required to have both (chrom AND genomeBuild) or sequenceId") 
        
        self.initParamValues ={
                'origCoordSystem': self.origCoordSystem,
                'seqType':  self.seqType,
                'allelicState': self.allelicState,
                'geneSymbol':geneSymbol,
                'hgncId':hgncId,
                'refAllele': self.refAllele,
                'altAllele': self.altAllele,        
                'chrom':self.chrom,
                'genomeBuild':self.genomeBuild,
                'start':self.start,
                'end':self.end,
                'sequenceId':self.sequenceId}

    def initParams(self):
        """ A dictionary of the initial parameters. 

        Returns:
            dict: A dictionary (Key: Initial parameters, Values: parameters values). 
        """
        return self.initParamValues
        
    def normalizedData(self):
        """A dictionary of the normalized data. This method checks to see if the initial parameters can be normalized and validated. 

        Raises:
            ValueError: If the origCoordSystem is not "0-based interbase"

        Returns:
            dict: A dictionary of the normalized data with validate attribute values. 
        """

        if self.initParamValues['origCoordSystem'] == "0-based interbase":
            self._validate_startCoord_endCoord()
            return {
            'origCoordSystem': self.origCoordSystem,
            'seqType':  self._validate_seqType(self.seqType),
            'allelicState': self._is_valid_allelicState(self.allelicState),
            'associatedGene': {'geneSymbol':self._is_valid_geneSymbol(self.geneSymbol),'hgncId':self._is_valid_hgncId(self.hgncId)},
            'refAllele': self._validate_ref_alt_allele(self.refAllele, 'refAllele'),
            'altAllele': self._validate_ref_alt_allele(self.altAllele,'altAllele'),        
            'position': {
                'chrom':self.chrom,
                'genomeBuild':self._validate_genomeBuild(self.genomeBuild),
                'start':self._validate_coordinates(self.start,'start'),
                'end':self._validate_coordinates(self.end,'end'),
                'sequenceId':self._validate_sequenceId(self.sequenceId)
                }
            }
        else:
            raise ValueError('Invalid origCoordSystem. Data can not be normalized')

    def _validate_origCoordSystem(self,origCoordSystem):
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
        if not value in allowedOrigCoordSystem:
            raise ValueError('Invalid origCoordSystem input: "{}". Allowed types: 0-based interbase, 0-based counting, or 1-based counting.'.format(coordSystem))
        return value
    
    def _validate_seqType(self,seqType):
        """ Validate seqType input. Method checks if the provided seqType is 
        one of the allowed types: ('DNA','RNA','PROTEIN'). 

        Args:
            seqType (str): The seqType to be validated. 

        Raises:
            ValueError: If the provided input is not one of the allowed types. 

        Returns:
            str: One of the allowed types in uppercase. 
        """
        value = seqType.strip().upper()
        allowedSeqType = ('DNA','RNA','PROTEIN')
        if not value in allowedSeqType:
            raise ValueError('Invalid seqType input: "{}". Allowed types: DNA, RNA, or PROTEIN (Case Insensitive).'.format( seqType)) 
        return value

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
            raise ValueError('Invalid {} input: "{}": is not an integer.'.format(attributeName,value))
        if value < 0:
            raise ValueError('Invalid {} input: "{}": is not greater then or equal to 0.'.format(attributeName,value))
        return value

    def _validate_startCoord_endCoord(self):
        """ Validate the start and end coordinate input. Method checks if the start coordinate is grater than or equal to the 
        end coordinate. 

        Raises:
            ValueError: If the start coordinate is greater than or equal to the end coordinate. 
        """
        if self.start >= self.end:
            raise ValueError("The start coordinate value can not be greater than or equal to the end coordinate value.")

    def _validate_ref_alt_allele(self,value,attributeName):
        """ Validate the refAllele and the altAllele input. Method checks if input value matches regular expression pattern (^[a-zA-Z0-9\s]*$).
        
        Args:
            value (str): The reference or alternative allele to be validated.
            attributeName (str): The name of the attribute that is being validated. Used for the error message.

        Raises:
            ValueError: If the provided value does not match regular expression pattern. 

        Returns:
            str: The validated reference and alternative allele input.
        """

        #NOTE: the regular expression that was originally: r'^[a-zA-Z\s]*$'.
        #  I added 0-9 because spdi expressions can have integers for Deletion and insertion. 

        pat = r'^[a-zA-Z0-9\s]*$'  
        if not re.match(pat, value.strip()) is not None:
            raise ValueError('Invalid {} input: "{}". Allowed types: string or empty string.'.format(attributeName,value))
        return value
    
    def _validate_chrom(self,chrom):
        """ Validate chrom input. Method checks if the provided chrom is one of the allowed types: ('1-22', X, Y, MT) or None.

        Args:
            chrom (str or None): The chrom to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str or None: One of the allowed types. 
        """
        allowedChrom = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
                         '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'MT')
        if chrom is None:
            return chrom
        value = chrom.strip().upper()
        if not value in allowedChrom:
            raise ValueError('Invalid chrom input: "{}". Allowed types: integer value of 1-22,X,Y or MT'.format(value))
        return value
    
    def _validate_genomeBuild(self,genomeBuild):
        """ Validate genomeBuild input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9]*$ or None.

        Args:
            genomeBuild (str or None): The genomeBuild to be validated.

        Raises:
            ValueError: If the provided input does not match regular expression pattern. 

        Returns:
            str or None: The validated genomeBuild value input. 
        """
        pat = r'^[a-zA-Z0-9]*$'
        if genomeBuild is None:
            return genomeBuild
        value = genomeBuild.strip()
        if not re.match(pat,value):
            raise ValueError('Invalid genomeBuild input: "{}". ALlowed types: alphanumeric characters only.'.format(value))
        return genomeBuild.strip()
    
    def _validate_sequenceId(self,sequenceId):
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
            raise ValueError('Invalid sequenceId input: "{}".ALlowed types: alphanumeric characters only.'.format(value))
        return value

    def _is_valid_allelicState(self,allelicState):
        """Validate allelicState input. Method checks if the provided allelicState is one of the allowed types: ('heterozygous','homozygous').

        Args:
            allelicState (str): The allelicState to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str: One of the allowed types in lowercase.
        """
        value = allelicState.strip().lower()
        allowed_allelicState = ('heterozygous','homozygous')
        if not value in allowed_allelicState:
            raise ValueError('Invalid allelicState input: "{}". Allowed types: Heterozygous, Homozygous (Case Insensitive).'.format(allelicState))
        return value

    def _is_valid_geneSymbol(self,geneSymbol):
        """Validate geneSymbol input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9]*$ .

        Args:
            geneSymbol (str): The geneSymbol to be validated.

        Raises:
            ValueError: If the provided input does not match regular expression pattern. 

        Returns:
            str: The validated geneSymbol value input. 
        """
        pat = r'^[a-zA-Z0-9]*$'
        value = geneSymbol.strip()
        if not re.match(pat,value):
            raise ValueError('Invalid geneSymbol input: "{}". Allowed type: alphanumeric characters only.'.format(value))
        return value

    def _is_valid_hgncId(self,hgncId):
        """ Validate the hgncId input. Method checks if the value is an integer and is greater than 1.

        Args:
            hgncId (int): The hgncId value to be validated. 

        Raises:
            ValueError: If the provided input is not an integer or less than 1. 

        Returns:
            int:  The validated hgncId value input. 
        """
        if not isinstance(hgncId,int):
            raise ValueError('Invalid hgncId input: "{}": is not an integer.'.format(hgncId))
        if hgncId < 1:
            raise ValueError('Invalid hgncId input: "{}": is not greater then or equal to 1.'.format(hgncId))
        return hgncId