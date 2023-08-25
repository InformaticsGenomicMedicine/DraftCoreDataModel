from src.api.ncbi_variation_services_api import VarServAPI

class SPDI:
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
        spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        return spdi_expression 

    def to_dict(self):
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