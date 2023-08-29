import re 

class CoreVariantClass:
    
    """ The CoreVariantClass is draft schema."""

    def __init__(self,origCoordSystem,seqType:str,refAllele:str,
                 #NOTE: changed alllelicState,geneSymbol and hgncID to optional
                  altAllele:str, start:int, end:int, allelicState:str=None,
                  geneSymbol:str=None, hgncId:int=None, chrom:str=None, 
                  genomeBuild:str=None, sequenceId:str=None,**kwargs):
        
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
                                   'notes':kwargs }

#TODO: https://github.com/InformaticsGenomicMedicine/DraftCoreDataModel/issues/10 
        self.origCoordSystem = self._validate_coordinates()
        self.seqType = self._validate_seqType()
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
        self.notes = kwargs
        
# # you can validate above:
#         self._validate_origCoordSystem()
#         self._validate_seqType()

        if not ((chrom and genomeBuild) or sequenceId):
            raise ValueError('Required to define either the pair (chrom AND genomeBuild) or sequenceId') 
        
        # self.initParamValues ={
        #         'origCoordSystem': self.origCoordSystem,
        #         'seqType':  self.seqType,
        #         'allelicState': self.allelicState,
        #         'geneSymbol':self.geneSymbol,
        #         'hgncId':self.hgncId,
        #         'refAllele': self.refAllele,
        #         'altAllele': self.altAllele,        
        #         'chrom':self.chrom,
        #         'genomeBuild':self.genomeBuild,
        #         'start':self.start,
        #         'end':self.end,
        #         'sequenceId':self.sequenceId}
        
    def initParams(self):
        """ A dictionary of the initial parameters. 

        Returns:
            dict: A dictionary (Key: Initial parameters, Values: parameters values). 
        """
        return self.initParamValues
        
    def normalizedData(self):
        """A dictionary of the normalized data. This method checks to see if the initial parameters can be normalized and validated. 

        Raises:
            ValueError: If the origCoordSystem is not "0-based interbase".

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

    def _validate_origCoordSystem(self):
        """ Validate origCoordSystem input. Method checks if the provided origCoordSystem
        is one of the allowed types: ('0-based interbase','0-based counting','1-based counting').

        Args:
            coordSystem (str): The origCoordSystem to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str: One of the allowed types. 
        """
        value = self.origCoordSystem.strip()
        allowedOrigCoordSystem = ('0-based interbase','0-based counting','1-based counting')
        if value not in allowedOrigCoordSystem:
            raise ValueError(f'Invalid origCoordSystem input: "{self.origCoordSystem}". Allowed types: {allowedOrigCoordSystem}.')
        self.origCoordSystem = value
    
    def _validate_seqType(self):
        """ Validate seqType input. Method checks if the provided seqType is one of the allowed types: ('DNA','RNA','PROTEIN'). 

        Args:
            seqType (str): The seqType to be validated. 

        Raises:
            ValueError: If the provided input is not one of the allowed types. 

        Returns:
            str: One of the allowed types in uppercase. 
        """
        value = self.seqType.upper().strip()
        allowedSeqType = ('DNA','RNA','PROTEIN')
        if value not in allowedSeqType:
            raise ValueError(f'Invalid seqType input: "{self.seqType}". Allowed types: {allowedSeqType} (Case Insensitive).') 
        self.origCoordSystem = value

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
        # return value

    def _validate_startCoord_endCoord(self):
        """ Validate the start and end coordinate input. Method checks if the start coordinate is grater than or equal to the 
        end coordinate. 

        Raises:
            ValueError: If the start coordinate is greater than or equal to the end coordinate. 
        """
        if self.start >= self.end:
            raise ValueError(f"The start coordinate value: {self.start} can not be greater than or equal to the end coordinate value {self.end}.")

    def _validate_ref_alt_allele(self,value,attributeName):
        """ Validate the refAllele and the altAllele input. Method checks if input value matches regular expression pattern (^[a-zA-Z0-9\s]*$).
        
        Args:
            value (str): The reference or alternative allele to be validated.
            attributeName (str): The name of the attribute that is being validated. Used for the error message.

        Raises:
            ValueError: If the provided value does not match regular expression pattern. 

        Returns:
            str: The validated reference or alternative allele input.
        """

        #NOTE: the regular expression that was originally: r'^[a-zA-Z\s]*$'.
        #  I added 0-9 because spdi expressions can have integers for Deletion and insertion. 

        pat = r'^[a-zA-Z0-9\s]*$'  
        if not re.match(pat, value.strip()) is not None:
            raise ValueError(f'Invalid {attributeName} input: "{value}". Allowed types: string or empty string.')
        # return value
    
    def _validate_chrom(self):
        """ Validate chrom input. Method checks if the provided chromosome is one of the allowed inputs: (1-22, X, Y, MT) or None.

        Args:
            chrom (str or None): The chrom to be validated.

        Raises:
            ValueError: If the provided input is not one of the allowed types.

        Returns:
            str or None: One of the allowed types. 
        """
        allowedChrom = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
                         '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'MT')
        if self.chrom is None:
            return self.chrom
        value = self.chrom.upper().strip()
        if not value in allowedChrom:
            raise ValueError(f'Invalid chrom input: "{self.chrom}". Allowed types: integer value of {allowedChrom}')
        
    
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
            raise ValueError(f'Invalid genomeBuild input: "{genomeBuild}". ALlowed types: alphanumeric characters only.')
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
            raise ValueError(f'Invalid sequenceId input: "{sequenceId}".ALlowed types: alphanumeric characters only.')
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
        value = allelicState.lower().strip()
        allowed_allelicState = ('heterozygous','homozygous')
        if value not in allowed_allelicState:
            raise ValueError(f'Invalid allelicState input: "{allelicState}". Allowed types: {allowed_allelicState} (Case Insensitive).')
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
            raise ValueError(f'Invalid geneSymbol input: "{geneSymbol}". Allowed type: alphanumeric characters only.')
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
            raise ValueError(f'Invalid hgncId input: "{hgncId}": is not an integer.')
        if hgncId < 1:
            raise ValueError(f'Invalid hgncId input: "{hgncId}": is not greater then or equal to 1.')
        return hgncId