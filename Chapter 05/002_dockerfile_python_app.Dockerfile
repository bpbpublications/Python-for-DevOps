# Script: 002_dockerfile_python_app.Dockerfile

# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Define environment variable
ENV NAME World

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run your application
CMD ["python", "app.py"]

# This Dockerfile is structured to build and run a Python application.
# - Base image: `python:3.9`.
# - Packages are installed from `requirements.txt`.
# - Application code is copied and made available at `/app`.
# - The application listens on port 80 and runs `app.py`.
