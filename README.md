# Kafka ETL Project with Cassandra Integration

This project demonstrates how to set up a data pipeline using Apache Kafka for real-time data ingestion, perform ETL processing on the data, and store the results in Apache Cassandra. The pipeline consists of a Kafka producer, a Kafka consumer, and integration with Cassandra.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup and Configuration](#setup-and-configuration)
- [Running the Kafka Producer](#running-the-kafka-producer)
- [Running the Kafka Consumer](#running-the-kafka-consumer)
- [Checking Data in Cassandra](#checking-data-in-cassandra)
- [Additional Notes](#additional-notes)

## Prerequisites

Before you begin, make sure you have the following installed and configured:

- Docker and Docker Compose
- Python 3.x
- `confluent-kafka` Python library
- `cassandra-driver` Python library

## Project Structure

- **`docker-compose.yml`**: Docker Compose configuration file for setting up Kafka, Cassandra, Kafka producer, and Kafka consumer containers.

- **`producer/`**: Directory containing the Kafka producer code.
  - **`Dockerfile`**: Dockerfile for building the Kafka producer container.
  - **`producer_code.py`**: Python code for the Kafka producer.

- **`consumer/`**: Directory containing the Kafka consumer code.
  - **`Dockerfile`**: Dockerfile for building the Kafka consumer container.
  - **`consumer_code.py`**: Python code for the Kafka consumer.

## Setup and Configuration

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd kafka-cassandra-etl

## Install the required Python packages:

    ```bash ```
    pip install confluent-kafka cassandra-driver 


Ensure Docker and Docker Compose are installed and running.

## Running the Kafka Producer

Build the Kafka producer container:

    ```bash```
    cd producer
    docker build -t kafka-producer .

Start the Docker containers for Kafka, Cassandra, and the Kafka producer:

    ```bash```
    docker-compose up -d

The Kafka producer will read data from data.json and publish messages to the Kafka topic input_topic.

## Running the Kafka Consumer

Build the Kafka consumer container:

    ```bash```
    cd consumer
    docker build -t kafka-consumer .

Start the Kafka consumer container:

    ```bash```
    docker-compose up -d


The Kafka consumer will consume messages from input_topic, perform ETL processing, and store the data in Cassandra.

## Checking Data in Cassandra

Access the Cassandra container's shell:

    ```bash```
    docker exec -it <cassandra-container-name> bash

Once inside the container's shell, start the Cassandra CQL shell:

    ```bash```
    cqlsh

Select the keyspace you want to work with:

    ```bash```
    USE my_keyspace;

Run CQL queries to check the data in Cassandra tables, e.g.,

    ```bash```
    SELECT * FROM merchandise_data;
Exit the cqlsh shell and the Cassandra container's shell when done.

Additional Notes
This is a simplified example for demonstration purposes. In a production environment, consider implementing robust error handling, monitoring, and scaling strategies.

Customize the Docker Compose configurations and container environment variables to match your specific setup and requirements.

Ensure that Kafka and Cassandra are properly configured for your use case, including replication and data retention policies.

Refer to the official documentation for Apache Kafka, Apache Cassandra, and Docker Compose for more advanced configurations and best practices.