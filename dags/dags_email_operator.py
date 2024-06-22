from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 6, 20, tz="Asia/Seoul"),                                                                                                                                                                                                                         
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'yoonjung107@gmail.com', 
        cc = 'hskimsky@gmail.com',
        subject = 'dag email operator by MKJJang airflow',
        html_content = '멍콩짱이 처음으로 보내는 Email Dag Operator Airflow 작업이 완료 되었습니다.'
    )