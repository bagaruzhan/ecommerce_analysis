import os
import pandas as pd
import sqlite3

def clean_column_names(df):
    new_cols = [col.strip().replace(' ', '_').replace('-', '_').replace('.', '_').lower() for col in df.columns]
    df.columns = new_cols
    return df

db_path = 'ecommerce_project.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

csv_folder = r'C:\Users\User\ecommerce-analysis\data'

for file_name in os.listdir(csv_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(csv_folder, file_name)
        table_name = os.path.splitext(file_name)[0].lower().replace('-', '_').replace(' ', '_')

        print(f"Loading file '{file_name}' into table '{table_name}'...")

        df = pd.read_csv(file_path, encoding='utf-8')
        df = clean_column_names(df)

        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Table '{table_name}' created successfully.")

conn.close()
print("SQLite connection closed.")
