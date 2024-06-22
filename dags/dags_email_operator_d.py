from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 * * *",
    start_date=pendulum.datetime(2024, 6, 22, tz="Asia/Seoul"),                                                                                                                                                                                                                         
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'yoonjung107@gmail.com', 
        cc = 'hskimsky@gmail.com',
        subject = 'dag email operator by MKJJang airflow',
        html_content = '멍콩짱이 보내는 daily batch email 이 도착하였습니다'
    )