# [Apache Airflow](https://airflow.apache.org/)

To run this project, you will need to install [Docker](https://www.docker.com/)

```bash
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
