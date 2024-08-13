#Database
class InjectionError(Exception):
    """Exception raised for error in the database injection process."""
    pass

# API Class

class SeqRepoDataProxyCreationError(Exception):
    """Exception raised for errors in translate HGVS expressions."""
    pass

# Translation Class
class HGVSTranslationError(Exception):
    """Exception raised for errors in translate HGVS expressions."""
    pass

class SPDITranslationError(Exception):
    """Exception raised for errors in translate SPDI expressions."""
    pass

class VRSTranslationError(Exception):
    """Exception raised for errors in translate VRS expressions."""
    pass

# Core Variant Class 
class InvalidInputConditionsError(ValueError):
    """Exception raised when the input conditions for chrom, genomeBuild, and sequenceId are not met."""
    pass

class InvalidCoordinateSystemError(ValueError):
    """Error is raised if the origCoordSystem provided does not match any of the expected values."""
    pass

class InvalidSequenceTypeError(ValueError):
    """Error is raised if the seqType provided does not match any of the expected values."""
    pass
    

class InvalidReferenceAlleleError(ValueError):
    """Error is raised if the refAllele provided does not match any of the expected regular expression patterns."""
    pass

class InvalidAlternativeAlleleError(ValueError):
    """Error is raised if the altAllele provided does not match any of the expected regular expression patterns."""
    pass

class InvalidCoordinateTypeError(TypeError):
    """Raised when the coordinate value is not an integer."""
    pass

class InvalidCoordinateValueError(ValueError):
    """Raised when the coordinate value is less than 0."""
    pass

class StartCoordinateGreaterThanEndError(ValueError):
    """Raised when the start value is greater than the end value."""
    pass

class InvalidAllelicStateError(ValueError):
    """Error is raised if the allelicState provided does not match any of the expected values."""
    pass

class InvalidGeneSymbolError(ValueError):
    """Error is raised if the geneSymbol provided does not match any of the expected regular expression patterns."""
    pass

class InvalidHGNCIdTypeError(TypeError):
    """Error is raised if the hgncId provided is not an integer."""
    pass

class InvalidHGNCIdError(ValueError):
    """Error is raised if the hgncId provided is less than 1."""
    pass

class InvalidChromosomeError(ValueError):
    """Error is raised if the chrom provided does not match any of the expected values."""
    pass

class InvalidGenomeBuildTypeError(TypeError):
    """Error is raised if the genomeBuild provided is not a string."""
    pass

class InvalidSequenceIdTypeError(TypeError):
    """Error is raised if the sequenceId provided is not a string."""
    pass