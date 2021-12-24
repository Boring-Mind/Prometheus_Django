# syntax=docker/dockerfile:1
FROM python:3.10.1-slim-buster as compile_step

# Install GCC to make hiredis
RUN apt-get update && apt-get install -y gcc

ENV DockerHOME=/app

# Create a working directory for Docker
RUN mkdir -p $DockerHOME

# Set the current working directory
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update Python package manager libraries and install Poetry
RUN pip3 install -U --no-cache-dir pip wheel setuptools poetry

# Install our projects' Python dependencies
COPY pyproject.toml ./poetry.lock* /
RUN poetry export -f requirements.txt --without-hashes -o $DockerHOME/requirements.txt

# Remove poetry when export is done
RUN pip3 uninstall poetry -y

# Install all dependencies
RUN pip3 install --no-cache-dir -r $DockerHOME/requirements.txt

FROM python:3.10.1-slim-buster as run_step

# Copy compiled Python dependencies from the previous step
COPY --from=compile_step \
    /usr/local/lib/python3.10/site-packages \
    /usr/local/lib/python3.10/site-packages

ENV DockerHOME=/app

# Copy whole project to docker home directory.
COPY . $DockerHOME

# Set the working directory
WORKDIR $DockerHOME/app