from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'name',
    'start_date': datetime(2024, 3, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag_a = DAG(
    'demo_dag',
    default_args=default_args,
    description='An bash example',
)

task1=BashOperator(
    task_id='first_task',
    bash_command='echo,Hello world,this is the first task',
    dag = dag_a
)

task2=BashOperator(
    task_id='second_task',
    bash_command='execute after the first task',
    dag=dag_a
)

task1>>task2