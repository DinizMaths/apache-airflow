from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def task_write(**kwarg):
  kwarg["ti"].xcom_push(key="xcom_value_1", value=10200)

def task_read(**kwarg):
  value = kwarg["ti"].xcom_pull(key="xcom_value_1")

  print(f"Value: {value}")

with DAG("dag_xcom", description="DAG 1", schedule_interval=None, start_date=datetime(2023, 7, 9), catchup=False) as dag:
  task1 = PythonOperator(task_id="tsk1", python_callable=task_write)
  task2 = PythonOperator(task_id="tsk2", python_callable=task_read)


  task1.set_downstream(task2)