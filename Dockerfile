# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install 

# Copy the rest of the application code to the container
COPY . .

# Expose the port your application will listen on
EXPOSE 5000

# Command to start the application
CMD ["python", "app.py"]
