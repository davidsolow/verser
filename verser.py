import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
db_params = {
    'dbname': os.environ['POSTGRES_DB'],
    'user': os.environ['POSTGRES_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': 'localhost',
    'port': '5432',
}

# Read SQL statements
with open('sql/create_tables.sql', 'r') as f:
    create_tables = f.read()

with open('sql/populate_data.sql', 'r') as f:
    populate_data = f.read()

# Connect to the database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Example: Create a table and insert data
    cursor.execute(create_tables)
    cursor.execute(populate_data)
    connection.commit()

except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
