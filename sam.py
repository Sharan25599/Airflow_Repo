from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'name',
    'start_date': datetime(2024, 3, 31),
    'retries': 1,
    'retry_delay': timedelta(seconds=1)
}

dag_a = DAG(
    'PARENT_DAG_1',
    default_args=default_args,
    description='An example Airflow DAG with three tasks',
)

def task1_function():
    print("Executing Task 1")


def task2_function():
    print("Executing Task 2")


def task3_function():
    print("Executing Task 3")


task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag_a
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=task2_function,
    dag=dag_a
)

task3 = PythonOperator(
    task_id='task3',
    python_callable=task3_function,
    dag=dag_a
)

task1 >> task2 >> task3
