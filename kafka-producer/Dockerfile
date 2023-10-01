FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install confluent-kafka

CMD ["python", "producer.py"]