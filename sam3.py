from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    'example_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 4, 2),
    catchup=False  # Setting catchup to False
)

# Define tasks
task1 = DummyOperator(
    task_id='task1',
    dag=dag
)
task2 = DummyOperator(
    task_id='task2',
    dag=dag
)

task1 >> task2