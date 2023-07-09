from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG("dag_trigger_1", description="My first DAG with Trigger Rule", schedule_interval=None, start_date=datetime(2023, 7, 9), catchup=False) as dag:

  task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
  task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
  task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", trigger_rule="one_failed")
  task4 = BashOperator(task_id="tsk4", bash_command="sleep 5", trigger_rule="none_failed")

  task3.set_upstream([task1, task2])
  task4.set_upstream(task3)