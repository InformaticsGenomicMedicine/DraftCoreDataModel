import psycopg2
from src.core_variant import CoreVariantClass
import os
from dotenv import load_dotenv
load_dotenv()
# TODO: look into SQLAlchemy python package for database connection


# TODO: test this code to make sure it is correct.
# TODO: not able to connect to database need to fix this

#TODO: this needs to be redone, i need to delete the hold database and create a new one. 

# class RequestLocalAPI:

#     HOSTNAME = os.getenv("HOSTNAME")
#     DATABASE = os.getenv("DATABASE")
#     USERNAME = os.getenv("USERNAME")
#     PWD = os.getenv("PWD")
#     PORTID = os.getenv("PORTID")

#     def __init__(self, hostname=None, database=None, username=None, pwd=None, portId=None):
#         self.hostname = hostname or self.HOSTNAME
#         self.database = database or self.DATABASE
#         self.username = username or self.USERNAME
#         self.pwd = pwd or self.PWD
#         self.portId = portId or self.PORTID
#         self.connect = None
#         self.cursor = None

#     def getExample(self, rowId):
#         """Retrieve a specific row in the database.

#         Args:
#             rowId (int): The rowId number.

#         Returns:
#             dict: A dictionary of the selected rowID from the database.
#         """
#         try:
#             self.connect = psycopg2.connect(
#                 host=self.hostname,
#                 dbname=self.database,
#                 user=self.username,
#                 password=self.pwd,
#                 port=self.portId,
#             )
#             self.cursor = self.connect.cursor()
#             self.cursor.execute(
#                 "SELECT * FROM core_variant_translation_demo WHERE id = {}".format(
#                     rowId
#                 )
#             )

#             row = self.cursor.fetchone()
#             attributeNames = [desc[0] for desc in self.cursor.description]

#             rowDict = {}
#             for i in range(len(attributeNames)):
#                 rowDict[attributeNames[i]] = row[i]

#             return rowDict

#         except Exception as e:
#             return e

#         finally:
#             if self.cursor is not None:
#                 self.cursor.close()
#             if self.connect is not None:
#                 self.connect.close()

#     def getAllExamples(self):
#         """Retrieve all examples from the database.

#         Returns:
#             list: A list containing all examples from the database.
#         """
#         try:
#             self.connect = psycopg2.connect(
#                 host=self.hostname,
#                 dbname=self.database,
#                 user=self.username,
#                 password=self.pwd,
#                 port=self.portId,
#             )
#             self.cursor = self.connect.cursor()
#             self.cursor.execute("SELECT * FROM core_variant_translation_demo")
#             return self.cursor.fetchall()

#         except Exception as e:
#             return e

#         finally:
#             if self.cursor is not None:
#                 self.cursor.close()
#             if self.connect is not None:
#                 self.connect.close()

#     def db_to_cvc(self, rowId):
#         """Converting a specific row from the database to a CoreVariantClass object.

#         Args:
#             rowId (int): The rowId number.

#         Returns:
#             dict: A dictionary of the database result as a CoreVariantClass object.
#         """
#         dbResult = self.getExample(rowId)
#         cvcValue = CoreVariantClass(
#             origCoordSystem=dbResult["origcoordsystem"],
#             seqType=dbResult["seqtype"],
#             refAllele=dbResult["refallele"],
#             altAllele=dbResult["altallele"],
#             start=dbResult["startcoord"],
#             end=dbResult["endcoord"],
#             allelicState=dbResult["allelicstate"],
#             geneSymbol=dbResult["genesymbol"],
#             hgncId=dbResult["hgncid"],
#             chrom=dbResult["chrom"],
#             genomeBuild=dbResult["genomebuild"],
#             sequenceId=dbResult["sequenceid"],
#         )
#         return cvcValue.init_params()
    


