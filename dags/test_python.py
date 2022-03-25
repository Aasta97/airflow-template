
from airflow.operators.python_operator import PythonOperator
from airflow import DAG

from datetime import datetime as dt
from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'start_date': dt(1970, 1, 1),
    'depends_on_past': False,
    "email": ["rximenez97@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    "test",
    default_args=default_args,
    schedule_interval="0 */12 * * *",
    catchup=False
)


def my_function(x):
    return x + " is a must have tool for Data Engineers."


t1 = PythonOperator(
    task_id='print',
    python_callable= my_function,
    op_kwargs = {"x" : "Apache Airflow"},
    dag=dag,
)


t1