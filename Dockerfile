FROM apache/airflow:2.1.0
COPY . /opt/airflow/
WORKDIR /opt/airflow/
USER airflow
RUN pip install -r requirements.txt