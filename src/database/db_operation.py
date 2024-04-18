import sqlite3
import pandas as pd
import json

class DbOperation:
    def __init__(self,db_file="goldstanddb.db"):
        self.db_file = db_file
        
    def _get_connection(self):
        return sqlite3.connect(self.db_file)
    
    def _deserialize_value(self,value):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    def get_combined_in_df(self):
        with self._get_connection() as con:
            df = pd.read_sql_query(f"SELECT * FROM CombineData", con)
        df['value'] = df['value'].apply(self._deserialize_value)
        return df 

    def extract_values(self,df,value_type):
        return df[df['name']==value_type]['value']

    def update_variation(self,id,xref,description):
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Variation SET xref = ?,description = ? WHERE id = ?", (xref,description,id))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Variation table: {str(e)}")
            
    def update_profile(self, id, name, version, description):
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Profile SET name=?, version=?, description = ? WHERE id = ?",(name, version, description,id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Profile table: {str(e)}")
            
    def update_expression(self, id, description, value):
        with self._get_connection() as con:
            try:
                con.execute("UPDATE Expression SET description = ?, value = ? WHERE id = ?",(description, value, id))
            except sqlite3.Error as e:
                raise ValueError(f"Error updating Expression table: {str(e)}")
            
    def delete_variation(self, id):
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Variation WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Variation table: {str(e)}")
            
    def delete_profile(self, id):
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Profile WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Profile table: {str(e)}")

    def delete_expression(self, id):
        with self._get_connection() as con:
            try:
                con.execute("DELETE FROM Expression WHERE id = ?",(id,))
            except sqlite3.Error as e:
                raise ValueError(f"Error deleting row in Expression table: {str(e)}")
            
    def get_variation(self, id):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Variation WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Variation table: {str(e)}")

    def get_profile(self, id):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Profile WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Profile table: {str(e)}")

    def get_expression(self, id):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Expression WHERE id = ?",(id,)).fetchone()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting row in Expression table: {str(e)}")

    def get_all_variations(self):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Variation").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Variation table: {str(e)}")
            
    def get_all_profiles(self):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Profile").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Profile table: {str(e)}")
            
    def get_all_expressions(self):
        with self._get_connection() as con:
            try:
                return con.execute("SELECT * FROM Expression").fetchall()
            except sqlite3.Error as e:
                raise ValueError(f"Error selecting all rows in Expression table: {str(e)}")
            