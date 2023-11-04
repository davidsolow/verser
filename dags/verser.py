from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from resources.scripts.get_policies import get_policies
from resources.scripts.update_postgres import update_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'verser_dag',
    default_args=default_args,
    description='A DAG to update PostgreSQL with new policies',
    schedule_interval='@daily',
    catchup=False,
)

def run_update_postgres():
    # You could potentially pass context if needed, but it's not used here
    new_policies = get_policies()  # Retrieve new policies
    update_postgres(new_policies)  # Update the database with new policies

update_postgres_task = PythonOperator(
    task_id='update_postgres',
    python_callable=run_update_postgres,
    dag=dag,
)
