import sqlite3
import json

class CreateTables:
    def __init__(self, db_file="goldstanddb.db"):
        self.db_file = db_file

    def _get_connection(self):
        return sqlite3.connect(self.db_file)

    def _create_tables(self):
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
        # Combing the talbes and this is what the user will use to look and brows the data.
        # reduce complexity
        combined_table = """
            CREATE VIEW IF NOT EXISTS CombineData AS
            SELECT p.name, p.version, v.xref, e.value 
            FROM Expression as e  
            LEFT JOIN Profile AS p ON e.profile_id = p.id 
            LEFT JOIN Variation AS v ON e.variation_id = v.id;
        """

        test_table = """
            CREATE VIEW IF NOT EXISTS TestData AS
            SELECT p.name, p.version, v.description, v.xref, e.value 
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
        for field in req_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

    def _serialize_value(self, data):
        if isinstance(data, dict):
            return json.dumps(data)
        else:
            return data

    def create_database(self):
        self._create_tables()

    def add_variation(self, data):
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
#     from src.database.data.profile_table_data import profile_data
#     from src.database.data.variation_table_data import variation_data
#     from src.database.data.expression_table_data import expression_data

#     db = CreateTables("gsdb.db")
#     db.create_database()

    # for var_data in variation_data:
    #     db.add_variation(var_data)
    # for prof_data in profile_data:
    #     db.add_profile(prof_data)
    # for expr_data in expression_data:
    #     db.add_expression(expr_data)
