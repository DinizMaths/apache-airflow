from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
  "depends_on_past": False,
  "start_date": datetime(2023, 7, 11),
  "retries": 1,
  "retry_delay": timedelta(seconds=10)
}

with DAG("dag_with_dict", description="My DAG With Groups", default_args=default_args, schedule_interval="@hourly", catchup=False, default_view="graph", tags=["Process", "Pipeline"]) as dag:
  task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
  task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
  task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")


  task1.set_downstream(task2)
  task2.set_downstream(task3)