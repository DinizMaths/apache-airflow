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

## [DAG 2](./dags/dag_2.py)

```bash
        ------> task2
      /
task1 
      \
        ------> task3
```

## [DAG 3](./dags/dag_3.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```

## [DAG 4](./dags/dag_4.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```