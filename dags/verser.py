import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
db_params = {
    'dbname': os.environ['POSTGRES_DB'],
    'user': os.environ['POSTGRES_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': 'verser-postgres',
    'port': '5432',
}

def update_postgres():
    # Read SQL statements
    with open('/opt/airflow/resources/sql/create_tables.sql', 'r') as f:
        create_tables = f.read()

    with open('/opt/airflow/resources/sql/populate_data.sql', 'r') as f:
        populate_data = f.read()

    # Connect to the database
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Create a table and insert data
        cursor.execute(create_tables)
        cursor.execute(populate_data)
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# DAG configuration
default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'verser',
    default_args=default_args,
    description='A simple DAG to update PostgreSQL',
    schedule_interval='@daily',
    catchup=False,
)

# Set up the PythonOperator to run your function
run_update = PythonOperator(
    task_id='update_postgres_task',
    python_callable=update_postgres,
    dag=dag,
)

# If there were other tasks, you'd set their order here. For now, it's just our one task.
