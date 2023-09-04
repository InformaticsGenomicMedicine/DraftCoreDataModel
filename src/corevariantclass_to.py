# from src.old_scripts.translate_class import translate_var_from_api

#TODO:
# Gen Std Core: this is the primary class we're working on now, to serve as the common data structure. The class needs to have the following methods.
# init: create an object from scratch using required params
# var_obj_to_core: takes as input a VRS, HGVS, or SPDI object, extracts values for required params, calls init()
# to_spdi( format ): returns a SPDI object, string, or dict ( { sequence, position, deletion, insertion } ) as determined by the value of "format"
# to_hgvs( format ): returns an HGVS object or string, as determined by the value of "format". This method can use the NCBI Var Services class to do the heavy lifting, or the hgvs package if we want to try to assemble it from scratch (probably harder)
# to_vrs( format ): returns a VRS object or JSON structure, as determined by the value of "format". This method can use the VICC class to do the heavy lifting.











# class cvc_translate:

#     def __init__(self):
#         """ Initialize translate class"""
#         self.translate = translate_var_from_api()

#     def unnorm_cvc_to_spdi(self,unnorm_cvc,format_type=True):
#         """Translate unnormalized CoreVariantClass dictionary into a SPDI expression string or dictionary.

#         Args:
#             unnorm_cvc (dict): CoreVariantClass dictionary to be translated
#             format_type (bool, optional): True returns string and False returns dictionary. Defaults to True.

#         Raises:
#             ValueError: If the format_type is not a boolean value.

#         Returns:
#             str or dict: If format_type is True a string SPDI expression is returned, else a dictionary SPDI expression is returned.
#         """
#         if not isinstance(format_type, bool):
#             raise ValueError('The format_type must be boolean: True or False.')

#         sequence = unnorm_cvc['sequenceId']
#         position = unnorm_cvc['start']
#         deletion = unnorm_cvc['refAllele']
#         insertion = unnorm_cvc['altAllele']

#         if format_type:
#             return f"{sequence}:{position}:{deletion}:{insertion}"
#         else:
#             return {
#                 'sequence_id':sequence,
#                 'position':position,
#                 'deletion': deletion,
#                 'insertion': insertion
#                 }

#     def norm_cvc_to_spdi(self,norm_cvc,format_type=True):
#         """Translate normalized CoreVariantClass dictionary into a SPDI Expression string or dictionary.

#         Args:
#             norm_cvc (dict): CoreVariantClass dictionary to be translated
#             format_type (bool, optional): True returns string and False returns dictionary. Defaults to True.

#         Raises:
#             ValueError: If the format_type is not a boolean value.

#         Returns:
#             str or dict: If format_type is True a string SPDI expression is returned, else a dictionary SPDI expression is returned.
#         """
#         if not isinstance(format_type, bool):
#             raise ValueError('The format_type must be boolean: True or False.')
        
#         sequence = norm_cvc['position']['sequenceID']
#         position = norm_cvc['position']['start']
#         deletion = norm_cvc['refAllele']
#         insertion = norm_cvc['altAllele']

#         if format_type:
#             return f"{sequence}:{position}:{deletion}:{insertion}"
#         else:
#             return {
#                 'sequence_id':norm_cvc['position']['sequenceID'],
#                 'position':norm_cvc['position']['start'],
#                 'deletion': norm_cvc['refAllele'],
#                 'insertion': norm_cvc['altAllele']
#                 }

#     def cvc_to_spdi(self,expression):
#         """Translate a CoreVariantClass dictionary into a SPDI expression.

#         Args:
#             expression (dict): The CoreVariantClass to be translated.

#         Raises:
#             ValueError: If the expression is not a unormalized CoreVariantClass dict or normalized CoreVariantClass dict.

#         Returns:
#             str: SPDI expression 
#         """
#         try:
#             cvc_to_spdi = self.unnorm_cvc_to_spdi(expression)
#         except Exception:
#             try:
#                 cvc_to_spdi = self.norm_cvc_to_spdi(expression)
#             except Exception:
#                 raise ValueError('Invalid expression, Allowed types: string unormalized CoreVariantClass dict or normalized CoreVariantClass dict')
#         return cvc_to_spdi
    
#     def cvc_to_hgvs(self,expression):
#         """Translate a CoreVariantClass dictionary into a right shift HGVS expression.

#         Args:
#             expression (dict): The CoreVariantClass to be translated. 

#         Returns:
#             str:  Right shift normalized HGVS expressions
#         """
#         spdi_expression = self.cvc_to_spdi(expression)
#         return self.translate.from_spdi_to_rightshift_hgvs(spdi_expression)

#     def cvc_to_norm_hgvs(self,expression):
#         """Translate a CoreVariantClass dictionary into a fully normalized HGVS expression.

#         Args:
#             expression (dict): The CoreVariantClass to be translated.

#         Returns:
#             str: Fully normalized HGVS expressions
#         """
#         spdi_expression = self.cvc_to_spdi(expression)
#         spdi_to_hgvs = self.translate.from_spdi_to_rightshift_hgvs(spdi_expression)
#         # Using Var-Norm API. 
#         hgvs_to_spdi =  self.translate.to_vrs_api(spdi_to_hgvs)
#         return self.translate.from_vrs_to_normalize_hgvs(hgvs_to_spdi)
        

#     def cvc_to_vrs(self,expression):
#         """Translate a CoreVariantClass dictionary into a VRS expression.

#         Args:
#             expression (dict): The CoreVariantClass to be translated.

#         Returns:
#             dict: VRS expression
#         """
#         spdi_expression = self.cvc_to_spdi(expression)
#         spdi_to_hgvs = self.translate.from_spdi_to_rightshift_hgvs(spdi_expression)    
#         return self.translate.to_vrs_api(spdi_to_hgvs)
