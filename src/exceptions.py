class HGVSTranslationError(Exception):
    """Exception raised for errors in translate HGVS expressions."""
    pass

# class SPDITranslationError(Exception):
#     """Exception raised for errors in translate SPDI expressions."""
#     pass

class InvalidInputConditionsError(ValueError):
    """Raised when the input conditions for chrom, genomeBuild, and sequenceId are not met."""
    pass


#TODO: Create MORE