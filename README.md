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

## [First DAG](./dags/first_dag.py)

```bash
task1 ------> task2 ------> tsak3
```

## [Second DAG](./dags/first_dag.py)

```bash
        ------> task2
      /
task1 
      \
        ------> task3
```

## [Third DAG](./dags/first_dag.py)

```bash
task1 ------>
              \
                ------> task3
              /
task2 ------>
```