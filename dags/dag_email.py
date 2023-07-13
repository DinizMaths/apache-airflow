from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta


default_args = {
  "depends_on_past": False,
  "start_date": datetime(2023, 7, 13),
  "email": ["<EMAIL1>"],
  "email_on_failure": True,
  "email_on_retry": False,
  "retries": 1,
  "retry_delay": timedelta(seconds=10)
}

with DAG("dag_email", description="My DAG that sends Email", default_args=default_args, schedule_interval="@hourly", catchup=False, default_view="graph", tags=["Process", "Pipeline"]) as dag:
  task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
  task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
  task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")
  task4 = BashOperator(task_id="tsk4", bash_command="exit 1")
  task5 = BashOperator(task_id="tsk5", bash_command="sleep 5", trigger_rule="none_failed")
  task6 = BashOperator(task_id="tsk6", bash_command="sleep 5", trigger_rule="none_failed")

  send_email = EmailOperator(
    task_id="send_email",
    to=["<EMAIL1>"],
    subject="Airflow Error",
    html_content="""
    <h3>ERROR</h3>
    <p>DAG: dag_email</p>
    """,
    trigger_rule="one_failed"
  )

  task3.set_upstream([task1, task2])
  task3.set_downstream(task4)
  task4.set_downstream([send_email, task5, task6])