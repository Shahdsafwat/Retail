from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def success_task():
    print("DBT PIPELINE COMPLETED SUCCESSFULLY")


with DAG(
    dag_id="snowflake_finance_pipeline",
    description="Run dbt models using dbt Core",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:
    DBT_PROJECT_DIR = "/usr/local/airflow/include/snowflake_data"

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt --no-partial-parse run --profiles-dir {DBT_PROJECT_DIR}",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --profiles-dir {DBT_PROJECT_DIR}",
    )

    dbt_success = PythonOperator(
        task_id="dbt_success",
        python_callable=success_task,
    )

dbt_run >> dbt_test >> dbt_success