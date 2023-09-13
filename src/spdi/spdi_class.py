from src.api.ncbi_variation_services_api import VarServAPI

#TODO: Write doc strings
class SPDI:
    """_summary_
    """
    def __init__(self,sequence,position,deletion,insertion):
        self.sequence = sequence
        self.position = position
        self.deletion = deletion
        self.insertion = insertion
        self.api = VarServAPI()

        spdi = f"{sequence}:{position}:{deletion}:{insertion}"
        try:
            self.api.validate_spdi(spdi)
        except Exception as e:
            raise e

    def to_string(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        return spdi_expression 

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            'sequence': self.sequence,
            'position':self.position,
            'deletion': self.deletion,
            'insertion': self.insertion
        }
    
        # self.val.validate_spdi(spdi_expression)

        # spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        # val_spdi_expression = self.val.validate_spdi(spdi_expression)
        # S,P,D,I = val_spdi_expression.split(':')