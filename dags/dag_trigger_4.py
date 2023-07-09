from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG("dag_trigger_4", description="My fourth DAG with Trigger Rule", schedule_interval=None, start_date=datetime(2023, 7, 9), catchup=False) as dag:

  task1 = BashOperator(task_id="tsk1", bash_command="exit 1")
  task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
  task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")
  task4 = BashOperator(task_id="tsk4", bash_command="sleep 5")
  task5 = BashOperator(task_id="tsk5", bash_command="sleep 5", trigger_rule="one_success")
  task6 = BashOperator(task_id="tsk6", bash_command="sleep 5")
  task7 = BashOperator(task_id="tsk7", bash_command="sleep 5")
  task8 = BashOperator(task_id="tsk8", bash_command="sleep 5")
  task9 = BashOperator(task_id="tsk9", bash_command="sleep 5", trigger_rule="one_failed")


  task1.set_downstream(task2)
  task3.set_downstream(task4)

  task5.set_upstream([task2, task4])

  task5.set_downstream(task6)
  task6.set_downstream([task7, task8, task9])