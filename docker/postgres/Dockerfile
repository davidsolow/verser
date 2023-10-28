# Use the official PostgreSQL image as the base image
FROM postgres:13

# Set environment variables if needed (e.g., the password)
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_USER myuser
ENV POSTGRES_DB mydatabase

# Copy initialization scripts (if you have any)
# These scripts run when the container starts and the database is initialized.
COPY ./init.sql /docker-entrypoint-initdb.d/
