import psycopg2
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from resources.configs.config import SQL_DIRECTORY


load_dotenv()

db_params = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': 'postgres',
    'port': '5432'
}

if None in db_params.values():
    raise ValueError("Database configuration is incomplete.")

sql_file_path = os.path.join(SQL_DIRECTORY, 'create_tables.sql')

def update_postgres(new_policies):
    if not new_policies or not all(isinstance(policy, dict) for policy in new_policies):
        print("No new policies to update or incorrect format.")
        return

    with open(sql_file_path, 'r') as f:
        create_tables = f.read()

    insert_statement = """
    INSERT INTO policies (  
                            policy_id,
                            policy_name,
                            policy_branch,
                            policy_type,
                            policy_url,
                            policy_text
                        )
    VALUES (
            %(policy_id)s,
            %(policy_name)s,
            %(policy_branch)s,
            %(policy_type)s,
            %(policy_url)s,
            %(policy_text)s)
    ;
    """

    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute(create_tables)
                for policy in new_policies:
                    cur.execute(insert_statement, policy)
                conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
