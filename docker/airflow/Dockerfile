# Use the official Airflow image as a base
FROM apache/airflow:2.2.3-python3.9

# Set the AIRFLOW_HOME environment variable (this is where configuration and DAG files will reside)
ENV AIRFLOW_HOME=/opt/airflow

# Switch back to the Airflow user
USER airflow

# Install any additional Python libraries using pip
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy over your DAGs and plugins
COPY dags/ ${AIRFLOW_HOME}/dags/
COPY plugins/ ${AIRFLOW_HOME}/plugins/

# If you have any other initialization steps or configurations, add them here

# The default command to execute when the container starts
CMD ["airflow", "scheduler", "&", "airflow", "webserver"]
