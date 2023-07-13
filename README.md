# [Apache Airflow](https://airflow.apache.org/)

To run this project, you will need to install [Docker](https://www.docker.com/)

```bash
sudo su
sudo chown <USER> ./dags/
docker-compose up -d
```
To login, just:

```bash
username: airflow
password: airflow
```

## [DAG 1](./dags/dag_1.py)

```bash
task1 ------> task2 ------> tsak3
```

```python
task1 >> task2 >> task3
```

## [DAG 2](./dags/dag_2.py)

```bash
        ------> task2
      /
task1 
      \
        ------> task3
```

```python
task1 >> [task2, task3]
```

## [DAG 3](./dags/dag_3.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```

```python
[task1, task2] >> task3
```

## [DAG 4](./dags/dag_4.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```

```python
task3.set_upstream([task1, task2])
```

## [Triggered DAG 1](./dags/dag_trigger_1.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```

```python
task1 = BashOperator(task_id="tsk1", bash_command="exit 1")

# Only executes if a previous one task failed. Will skip if no one was failed
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", trigger_rule="one_failed")


task3.set_upstream([task1, task2])
```

## [Triggered DAG 2](./dags/dag_trigger_2.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```

```python
task1 = BashOperator(task_id="tsk1", bash_command="exit 1")
task2 = BashOperator(task_id="tsk2", bash_command="exit 1")

# Only executes if all previous tasks was failed
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", trigger_rule="all_failed")


task3.set_upstream([task1, task2])
```

## [Triggered DAG 3](./dags/dag_trigger_3.py)

```bash
task1 ------>
              \
                ------> task3 ------> task4
              /
task2 ------>
```

```python
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", trigger_rule="one_failed")

# Only executes if no one previous task was failed
task4 = BashOperator(task_id="tsk4", bash_command="sleep 5", trigger_rule="none_failed")

task3.set_upstream([task1, task2])
task4.set_upstream(task3)
```

## [Triggered DAG 4](./dags/dag_trigger_4.py)

```bash
task1 ------> task2 ------>                                 ------> task7
                            \                             /
                              ------> task5 ------> task6 --------> task8
                            /                             \
task3 ------> task4 ------>                                 ------> task9
```

```python
task5 = BashOperator(task_id="tsk5", bash_command="sleep 5", trigger_rule="one_success")
task9 = BashOperator(task_id="tsk9", bash_command="sleep 5", trigger_rule="one_failed")

task1.set_downstream(task2)
task3.set_downstream(task4)

task5.set_upstream([task2, task4])

task5.set_downstream(task6)
task6.set_downstream([task7, task8, task9])
```

## [DAG with Groups](./dags/dag_group.py)

```bash
 ---------------------                                                  -------
| task1 ------> task2 |------>                                 ------> | task7 |
 ---------------------         \                             /         |       |
                                 ------> task5 ------> task6 --------> | task8 |
                               /                             \         |       |
task3 --------> task4 ------->                                 ------> | task9 |
                                                                        -------
``` 

```python
with TaskGroup("tsk_group1") as group:
  task1 = BashOperator(task_id="tsk1", bash_command="exit 1")
  task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")

with TaskGroup("tsk_group") as group:
  task7 = BashOperator(task_id="tsk7", bash_command="sleep 5")
  task8 = BashOperator(task_id="tsk8", bash_command="sleep 5")
  task9 = BashOperator(task_id="tsk9", bash_command="sleep 5", trigger_rule="one_failed")


task1.set_downstream(task2)
task3.set_downstream(task4)

task5.set_upstream([task2, task4])

task5.set_downstream(task6)
task6.set_downstream([task7, task8, task9])
```

## DAG that runs other DAG

NOTE: **dag_trigger_dag_2** needs to be **unpaused**

```bash
 ----dag_trigger_dag_1----          ----dag_trigger_dag_2----
|                         |        |                         |
|  task1 -------> task2 --|------> |  task1 --------> task2  |
|                         |        |                         |
 -------------------------          -------------------------
``` 

[Dag 1](./dags/dag_trigger_dag_1.py)
```python
# dag_trigger_dag_1.py

task2 = TriggerDagRunOperator(task_id="tsk2", trigger_dag_id="dag_trigger_dag_2")


task1.set_downstream(task2)
```

[Dag 2](./dags/dag_trigger_dag_2.py)
```python
# dag_trigger_dag_2.py

task1.set_downstream(task2)
```

## [DAG with Dict](./dags/dag_with_dict.py)

```bash
task1 ------> task2 ------> tsak3
```

```python
task1.set_downstream(task2)
task2.set_downstream(task3)
```

## [DAG with XCOM](./dags/dag_xcom.py)

```bash
task1 ------> task2
```

```python
def task_write(**kwarg):
  kwarg["ti"].xcom_push(key="xcom_value_1", value=10200)

def task_read(**kwarg):
  value = kwarg["ti"].xcom_pull(key="xcom_value_1")


task1 = PythonOperator(task_id="tsk1", python_callable=task_write)
task2 = PythonOperator(task_id="tsk2", python_callable=task_read)


task1.set_downstream(task2)
```