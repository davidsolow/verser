# Use the official Airflow image as a parent image
FROM apache/airflow:latest

# Set the working directory in the container
WORKDIR /opt/airflow

# Copy the requirements.txt file into the container at /opt/airflow
COPY requirements.txt ./

# Install any dependencies in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt
