from src.api.ncbi_variation_services_api import var_serv_api

class SPDI:
    def __init__(self,sequence,position,deletion,insertion):
        self.sequence = sequence
        self.position = position
        self.deletion = deletion
        self.insertion = insertion
        self.val = var_serv_api()
    
    def to_string(self):
        spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        return self.val.validate_spdi(spdi_expression)

    def to_dict(self):
        
        spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        val_spdi_expression = self.val.validate_spdi(spdi_expression)
        S,P,D,I = val_spdi_expression.split(':')
        return {
            'sequence': S,
            'position':P,
            'deletion': D,
            'insertion': I
        }