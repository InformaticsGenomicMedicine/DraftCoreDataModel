import sqlite3
import json

class CreateTables:
    def __init__(self, db_file="database_name.db"):
        self.db_file = db_file

    def _get_connection(self):
        """ Establish a connection to the the database. 

        Returns:
            sqlite3.Connection: A connection object to the SQLite database.
        """
        return sqlite3.connect(self.db_file)

    def _create_tables(self):
        """ Creates database tables and views required for storing variation, profile, and expression data.
            The method ensures tables and views are created only if they do not already exist in the database. 

                - Variation table: Stores variations with fields for id, xref, and description.  
                - Profile table: Stores profiles with fields for id, name, version, and description.
                - Expression table: Stores expressions with fields for id, variation_id, profile_id, description, and value.
                - CombineData view: A view that combines data from the Expression (value), Profile (name, version), and Variation (description, xref) tables. 
                - TestData View: A view that combines data from the Expression (value), Profile (name, version), and Variation (xref) tables. 
        """        
        # Variation table schema
        variation_table = """
            CREATE TABLE IF NOT EXISTS Variation (
            id INTEGER PRIMARY KEY,
            xref TEXT,
            description TEXT
            )
        """
        # Profile table schema
        profile_table = """
            CREATE TABLE IF NOT EXISTS Profile (
                id INTEGER PRIMARY KEY,
                name TEXT,
                version TEXT,
                description TEXT
            ) 
            """
        # Expression table schema
        expression_table = """
            CREATE TABLE IF NOT EXISTS Expression (
            id INTEGER PRIMARY KEY,
            variation_id INTEGER,
            profile_id INTEGER,
            description TEXT,
            value TEXT,
            FOREIGN KEY (variation_id) REFERENCES Variation(id),
            FOREIGN KEY (profile_id) REFERENCES Profile(id)
            )
        """
        # Combing the tables and this is what the user will use to look and brows the data.
        # reduce complexity
        combined_table = """
            CREATE VIEW IF NOT EXISTS CombineData AS
            SELECT p.name, p.version, v.description, v.xref, e.value 
            FROM Expression as e  
            LEFT JOIN Profile AS p ON e.profile_id = p.id 
            LEFT JOIN Variation AS v ON e.variation_id = v.id;
        """

        test_table = """
            CREATE VIEW IF NOT EXISTS TestData AS
            SELECT p.name, p.version, v.xref, e.value 
            FROM Expression as e  
            LEFT JOIN Profile AS p ON e.profile_id = p.id 
            LEFT JOIN Variation AS v ON e.variation_id = v.id;
        """

        with self._get_connection() as con:
            con.execute(variation_table)
            con.execute(profile_table)
            con.execute(expression_table)
            con.execute(combined_table)
            con.execute(test_table)

    def _validate_input(self, data, req_fields):
        """ Validate if required fields are present in the data dictionary. 

        Args:
            data (dict): The input data dictionary to validate. 
            req_fields (list): A list of strings representing required field names. 

        Raises:
            ValueError: Raised if any required field is missing in the data dictionary.
        """
        for field in req_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

    def _serialize_value(self, data):
        """ Serializes the input data into json format if it is a dictionary.

        Args:
            data (dict): The data to serialize. 

        Returns:
            str: Returns the serialized Json string if `data` is a dictionary, otherwise returns the input data unchanged. 
        """
        if isinstance(data, dict):
            return json.dumps(data)
        else:
            return data

    def create_database(self):
        """ Creates tables and views in the database. Method internally calls `_create_tables` to initialize database tables and views. 
        """
        self._create_tables()

    def add_variation(self, data):
        """ Adds a new variation entry to the Variation table in the database.

        Args:
            data (dict): A dictionary containing `xref` and `description` fields.

        Raises:
            RuntimeError: If there is an error inserting variation data into the database.
        """
        self._validate_input(data, ["xref", "description"])
        with self._get_connection() as con:
            try:
                con.execute(
                    "INSERT INTO Variation (xref,description) VALUES (?,?)",
                    (data["xref"], data["description"]),
                )
            except sqlite3.Error as e:
                raise RuntimeError(f"Error inserting variation data: {str(e)}")

    def add_profile(self, data):
        """ Adds a new profile entry to the Profile table in the database.

        Args:
            data (dict): A dictionary containing `name`, `version`, and `description` fields.

        Raises:
            RuntimeError: if there is an error inserting profile data into the database.
        """
        self._validate_input(data, ["name", "version", "description"])
        with self._get_connection() as con:
            try:
                con.execute(
                    "INSERT INTO Profile (name,version,description) VALUES (?,?,?)",
                    (data["name"], data["version"], data["description"]),
                )
            except sqlite3.Error as e:
                raise RuntimeError(f"Error inserting profile data: {str(e)}")

    def add_expression(self, data):
        """ Adds a new expression entry to the Expression table in the database. 

        Args:
            data (dict): A dictionary containing `variation_id`, `profile_id`, `description`, and `value` fields.

        Raises:
            ValueError: If the provided variation_id or profile_id does not exist in their respective tables.
            RuntimeError: If there is an error inserting expression data into the database.
        """
        self._validate_input(
            data, ["variation_id", "profile_id", "description", "value"]
        )

        with self._get_connection() as con:
            try:
                variation_row = con.execute(
                    "SELECT id FROM Variation WHERE id = ?", (data["variation_id"],)
                ).fetchone()
                if not variation_row:
                    raise ValueError(
                        f"Error: Variation with the provided ID {data['variation_id']} does not exist."
                    )

                profile_row = con.execute(
                    "SELECT id FROM Profile WHERE id = ?", (data["profile_id"],)
                ).fetchone()
                if not profile_row:
                    raise ValueError(
                        f"Error: Profile with the provided ID {data['profile_id']} does not exist."
                    )
                
                # need to serialize vrs and cvc dictionary  
                value = self._serialize_value(data["value"])

                con.execute(
                    "INSERT INTO Expression (variation_id,profile_id,description,value) VALUES (?,?,?,?)",
                    (
                        data["variation_id"],
                        data["profile_id"],
                        data["description"],
                        value,
                    ),
                )
            except sqlite3.Error as e:
                raise RuntimeError(f"Error inserting expression data: {str(e)}")
            
# if __name__ == "__main__":
#     from db_creation import CreateTables
#     from database.data.profile_table_data import profile_data
#     from database.data.variation_table_data import variation_data
#     from database.data.expression_table_data import expression_data

#     db = CreateTables("gsdb_v2.db")
#     db.create_database()

#     for var_data in variation_data:
#         db.add_variation(var_data)
#     for prof_data in profile_data:
#         db.add_profile(prof_data)
#     for expr_data in expression_data:
#         db.add_expression(expr_data)
