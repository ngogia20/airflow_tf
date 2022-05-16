from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

import requests
import json


# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('NS_OCI',
         start_date=datetime(2021, 1, 1),
         max_active_runs=2,
         schedule_interval=timedelta(minutes=30),
         default_args=default_args,
         catchup=False
         ) as dag:




    provision = BashOperator(
        task_id='provison_vm',
        bash_command='scripts/tfp.sh',
    )
    export = BashOperator(
        task_id='export_variable',
        bash_command='scripts/tfv.sh',
    )

    provision >> export
