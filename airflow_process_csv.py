from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; use to instantiate a DAG
from airflow import DAG
# Operators
from airflow.operators.bash import BashOperator


with DAG(
    'tutorial',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'execution_timeout': timedelta(seconds=300),
    },
    description='A simple DAG',
    # runs every day at 1.30am (a buffer time of half an hour)
    schedule_interval='30 1 * * *',
    start_date=datetime(2022,6,26,1,30),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id='process_csv',
        bash_command = 'python /home/airflow/airflow/dags/scripts/process_csv.py {{ dag_run.conf["filename"] if dag_run else '' }}',
    )