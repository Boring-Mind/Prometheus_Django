# syntax=docker/dockerfile:1
FROM python:3.10.1-slim-buster

ENV DockerHOME=/app

# Create a working directory for Docker
RUN mkdir -p $DockerHOME

# Set the current working directory
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update Python package manager libraries and install Poetry
RUN pip3 install -U pip wheel setuptools poetry

# Install our projects' Python dependencies
COPY pyproject.toml ./poetry.lock* /
RUN poetry export -f requirements.txt --without-hashes -o $DockerHOME/requirements.txt

# Install all dependencies
RUN pip3 install --no-cache-dir -r $DockerHOME/requirements.txt

# Copy whole project to docker home directory.
COPY . .

WORKDIR $DockerHOME/app