from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pendulum

import sys
sys.path.insert(0, '/root/airflow/parser')
from main import main

dag = DAG(
    "main",
    #start_date = days_ago(0,0,0,0,0),
    start_date = pendulum.today("UTC").add(days=0),
    tags = ["python"]
)

get_data = PythonOperator(
    task_id='get_data',
    python_callable=main,
    dag = dag,
)

get_data