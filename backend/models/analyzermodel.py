import pandas as pd
import sqlite3

class AnalyzerCvModel:
    def categorized_cv(self):
        db_path = '../dataset/CVs_dataset.sqlite3'
        con = sqlite3.connect(db_path)
        query = 'SELECT * FROM cvs_data'
        df = pd.read_sql_query(query, con)
        con.close()
        
        
demo = AnalyzerCvModel()
demo.categorized_cv()

    