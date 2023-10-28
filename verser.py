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
    'host': 'localhost',  # Assuming PostgreSQL is running on localhost
    'port': '5432',       # Port where PostgreSQL is exposed
}

# Connect to the database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Example: Create a table and insert data
    cursor.execute('CREATE TABLE IF NOT EXISTS sample_data (id serial PRIMARY KEY, data text);')
    cursor.execute('INSERT INTO sample_data (data) VALUES (%s);', ('Hello, PostgreSQL!',))
    connection.commit()

except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
