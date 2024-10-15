import os
import sqlite3

class CvModel:
    def __init__(self, path='../data'):
        self.path = path
        self.all_cvs = self.get_subfolders_and_cvs(path)
        self.db_name = '../dataset/CVs_dataset.sqlite3'
    
    def get_subfolders_and_cvs(self, path):
        # List to hold dictionaries with subfolder names as keys and CV files as values
        cvs_by_occupation = []

        # Traverse the data folder to get subfolders and files
        for root, dirs, files in os.walk(path):
            # Get the name of the current subfolder (relative to 'data' folder)
            subfolder_name = os.path.basename(root)

            # Skip the root directory (if you only want subfolders)
            if root == path:
                continue

            # Get all CV files in the current subfolder
            cv_files = [file for file in files if file.endswith(('.pdf', '.docx', '.txt'))]  # Add relevant file extensions

            # Only add if there are CV files in the subfolder
            if cv_files:
                # Create a dictionary where the subfolder name is the key, and the CVs are the value
                cvs_by_occupation.append({subfolder_name: cv_files})

        return cvs_by_occupation
    # for debug -- to show that subfolders is a list
    def print_all_cvs(self):
        # Print all CVs by subfolder (occupation)
        print(self.all_cvs)
        return self.all_cvs
    # only to create the db
    def create_db_table(self):
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS cvs_data (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           proffesion TEXT NOT NULL,
                           cv_file TEXT NOT NULL
                       )
                 ''')
        con.commit()
        con.close()
    # from now - there is db with all candidates with paths to the cv's files
    def save_in_db(self):
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        
        for pro in self.all_cvs:
            for sub, files in pro.items():
                for file in files:
                    file_path = f'data/{sub}/{file}'
                    cursor.execute('INSERT INTO cvs_data (proffesion, cv_file) VALUES (?, ?)', (sub,file_path))
                    
        con.commit()
        con.close()
        
    def clear_table(self):
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        # Delete all rows from the table
        cursor.execute('DELETE FROM cvs_data')
        con.commit()
        con.close()
    
    
# Example usage
demo = CvModel()
demo.save_in_db()
