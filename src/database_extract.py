import psycopg2
from src.core_variant import CoreVariantClass


class request_local_api:

    def __init__(self,hostname='localhost',database='DemoCoreLiteDB',username='sal_test',pwd='admin',portId='5432'):
        """Initialize the local database connection attributes.

        Args:
            hostname (str, optional): The hostname of the database server. Defaults to 'localhost'.
            database (str, optional): The name of the database. Defaults to 'DemoCoreLiteDB'.
            username (str, optional): The username of the database. Defaults to 'sal_test'.
            pwd (str, optional): The password of the database. Defaults to 'admin'.
            portId (str, optional): The port number. Defaults to '5432'.
        """

        self.hostname = hostname
        self.database = database
        self.username = username
        self.pwd = pwd
        self.portId = portId

    def getExample(self,rowId):
        """Retrieve a specific row in the database. 

        Args:
            rowId (int): The rowId number. 

        Returns:
            dict: A dictionary of the selected rowID from the database. 
        """
        try:
            self.connect = psycopg2.connect(host = self.hostname, dbname = self.database, user = self.username, password = self.pwd, port = self.portId) 
            self.cursor = self.connect.cursor()
            self.cursor.execute('SELECT * FROM core_variant_translation_demo WHERE id = {}'.format(rowId))

            row = self.cursor.fetchone()  
            attributeNames = [desc[0] for desc in self.cursor.description]

            rowDict = {}
            for i in range(len(attributeNames)):
                rowDict[attributeNames[i]] = row[i]

            return rowDict

        except Exception as e:
            return e

        finally: 
            self.cursor.close()
            self.connect.close()

    def getAllExamples(self):
        """Retrieve all examples from the database. 

        Returns:
            list: A list containing all examples from the database.
        """
        try:
            self.connect = psycopg2.connect(host = self.hostname, dbname = self.database, user = self.username, password = self.pwd, port = self.portId)
            self.cursor = self.connect.cursor() 
            self.cursor.execute('SELECT * FROM core_variant_translation_demo')
            return self.cursor.fetchall()
         
        except Exception as e:
            return e
        
        finally: 
            self.cursor.close()
            self.connect.close()
            
    def db_to_cvc(self,rowId):
        """Converting a specific row from the database to a CoreVariantClass object.

        Args:
            rowId (int): The rowId number. 

        Returns:
            dict: A dictionary of the database result as a CoreVariantClass object. 
        """
        dbResult = self.getExample(rowId)
        cvcValue = CoreVariantClass(origCoordSystem= dbResult['origcoordsystem'],
                                    seqType=dbResult['seqtype'], refAllele=dbResult['refallele'],
                                    altAllele=dbResult['altallele'], start=dbResult['startcoord'],
                                    end=dbResult['endcoord'], allelicState = dbResult['allelicstate'],
                                    geneSymbol = dbResult['genesymbol'], hgncId = dbResult['hgncid'], 
                                    chrom=dbResult['chrom'],genomeBuild=dbResult['genomebuild'],sequenceId=dbResult['sequenceid'])
        return cvcValue.initParams()