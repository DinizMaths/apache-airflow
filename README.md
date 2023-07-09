# apache-airflow

## [First DAG](./dags/first_dag.py)

```
task1 ------> task2 ------> tsak3
```

## [Second DAG](./dags/first_dag.py)

```
        ------> task2
      /
task1 
      \
        ------> task3
```

## [Third DAG](./dags/first_dag.py)

```
task1 ------>
              \
                ------> task3
              /
task2 ------>
```