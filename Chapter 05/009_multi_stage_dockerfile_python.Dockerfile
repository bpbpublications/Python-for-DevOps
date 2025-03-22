# Script: 009_multi_stage_dockerfile_python.Dockerfile

# Stage 1: Build stage with a minimal base image
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* /root/.cache/pip

# Add your application code
COPY . .

# Build your application (replace this with your build command if applicable)
RUN python build.py

# Stage 2: Create a final production image with a minimal base image
FROM python:3.9-slim AS production

# Set the working directory
WORKDIR /app

# Copy only the necessary artifacts from the builder stage
COPY --from=builder /app/ /app/

# Expose the port your application will run on
EXPOSE 8080

# Start your application (replace this with your startup command)
CMD ["python", "app.py"]

# This multi-stage Dockerfile is optimized for building and running a Python application:
# - Stage 1 (builder): Installs dependencies, includes the application code, and performs the build process.
# - Stage 2 (production): Creates a lightweight production-ready image by copying only the necessary artifacts from the builder stage.
