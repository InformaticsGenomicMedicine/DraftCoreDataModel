import sqlite3
import pandas as pd
import json

class DbOperation:
    def __init__(self,db_file="filename.db"):
        self.db_file = db_file
        
    def _get_connection(self):
        """ Establish a connection to the the database. 

        Returns:
            sqlite3.Connection: A connection object to the SQLite database.
        """
        return sqlite3.connect(self.db_file)
    
    def _deserialize_value(self,value):
        """ Deserializes a JSON string into python objects.

        Args:
            value (str): The JSON string to deserialize.

        Returns:
            object: The deserialized python object.
        """
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    def get_combined_in_df(self):
        """ Retrieves data from the CombineData view in the database and returns it as a Pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing data from the CombineData view. 
        """
        with self._get_connection() as con:
            df = pd.read_sql_query(f"SELECT * FROM CombineData", con)
        df['value'] = df['value'].apply(self._deserialize_value)
        return df 
    
    def get_testdata_df(self): 
        """ Retrieves data from the TestData view in the database and returns it as a Pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing data from the TestData view. 
        """
        with self._get_connection() as con: 
            df = pd.read_sql_query(f"SELECT * FROM TestData",con)
        df['value'] = df['value'].apply(self._deserialize_value)

        #will create a DataFrame where each row has a unique combination of 'description' and 'xref', and the 'cvc', 'spdi', 'hgvs',
        # and 'vrs' columns contain the corresponding 'value' for that combination.
        pivot_df = df.pivot_table(index=['xref'], columns='name', values='value', aggfunc='first').reset_index()

        # Convert the DataFrame to a list of dictionaries
        result_list = pivot_df.to_dict('records')

        return result_list

    def extract_values(self,df,value_type):
        """ Extracts values from a DataFrame based on the specific value_type. 

        Args:
            df (pd.DataFrame): The DataFrame containing the data.
            value_type (str): The type of value to extract.

        Returns:
            pd.Series: A pandas Series containing the extracted values. 
        """
        return df[df['name']==value_type]['value']

    def update_variation(self,id,xref,description):
        """ Update an existing variation record in the Variation table. 

        Args:
            id (int): The ID of the variation record to update. 
            xref (str): The new xref value. 
            description (str): The new description value. 

        Raises:
            ValueError: If there is an error updating the variation table. 
        """
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Variation SET xref = ?,description = ? WHERE id = ?", (xref,description,id))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Variation table: {str(e)}")
            
    def update_profile(self, id, name, version, description):
        """ Update an existing profile record in the Profile table. 

        Args:
            id (int): The ID of the profile record to update. 
            name (str): The new name value. 
            version (str): The new version value. 
            description (str): The new description value. 

        Raises:
            ValueError: If there is an error updating the Profile table. 
        """
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Profile SET name=?, version=?, description = ? WHERE id = ?",(name, version, description,id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Profile table: {str(e)}")
            
    def update_expression(self, id, description, value):
        """ Update an existing expression record in the Expression table. 

        Args:
            id (int): The ID of the expression record to update.
            description (str): The new description value. 
            value (str): The new value (serialized json string).

        Raises:
            ValueError: If there is an error updating the expression table. 
        """
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Expression SET description = ?, value = ? WHERE id = ?",(description, value, id))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Expression table: {str(e)}")
            
    def delete_variation(self, id):
        """ Deletes a variation record form the Variation table.

        Args:
            id (int): The ID of the variation record to delete. 

        Raises:
            ValueError: If there is an error deleting the row from the Variation table. 
        """
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Variation WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Variation table: {str(e)}")
            
    def delete_profile(self, id):
        """ Deletion a profile record from the Profile table. 

        Args:
            id (int): The ID of the profile record to delete.

        Raises:
            ValueError: If there is an error deleting the row from the Profile table.
        """
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Profile WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Profile table: {str(e)}")

    def delete_expression(self, id):
        """ Deletion an expression record from the Expression table. 

        Args:
            id (int): The ID of the expression record to delete.

        Raises:
            ValueError: If there is an error deleting the row from the Expression table.
        """
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Expression WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Expression table: {str(e)}")
            
    def get_variation(self, id):
        """ Retrieves a variation record from the Variation table based on the ID. 

        Args:
            id (int): The ID of the variation record to retrieve. 

        Raises:
            ValueError: If there is an error selecting the row from the Variation table.

        Returns:
            tuple: A tuple representing the variation record. 
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Variation WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Variation table: {str(e)}")

    def get_profile(self, id):
        """ Retrieves a profile record from the Profile table based on the ID.

        Args:
            id (int): The ID of the profile record to retrieve. 

        Raises:
            ValueError: If there is an error selecting the row from the Profile table.

        Returns:
            tuple: A tuple representing the profile record. 
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Profile WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Profile table: {str(e)}")

    def get_expression(self, id):
        """ Retrieves a expression record from the Expression table based on the ID.

        Args:
            id (int): The ID of the expression record to retrieve. 

        Raises:
            ValueError: If there is an error selecting the row from the Expression table.

        Returns:
            tuple: A tuple representing the expression record. 
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Expression WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Expression table: {str(e)}")

    def get_all_variations(self):
        """ Retrieves all variations records from the Variation table. 

        Raises:
            ValueError: If there is an error selecting all rows from the Variation table. 

        Returns:
            list: A list of tuples, where each tuple represents a variation record.
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Variation").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Variation table: {str(e)}")
            
    def get_all_profiles(self):
        """ Retrieves all profile records from the Profile table. 

        Raises:
            ValueError: If there is an error selecting all rows from the Profile table.

        Returns:
            list: list: A list of tuples, where each tuple represents a profile record.
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Profile").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Profile table: {str(e)}")
            
    def get_all_expressions(self):
        """ Retrieves all expression records from the Expression table.

        Raises:
            ValueError: If there is an error selecting all rows from the Expression table.

        Returns:
            list: list: A list of tuples, where each tuple represents a expression record.
        """
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Expression").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Expression table: {str(e)}")
            