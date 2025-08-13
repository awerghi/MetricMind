import json
import time
import logging

from confluent_kafka import Producer

from conf.log import logger



def connect_to_kafka(bootstrap_servers: str, number_of_retries: int):
    for attempt in range(number_of_retries):
        try:
            producer = Producer({'bootstrap.servers': bootstrap_servers})
            logger.info("✅ Connected to Kafka")
            return producer
        except Exception as e:
            logger.info(f"⏳ Kafka not ready yet, retrying... {e}")
            time.sleep(5)
    else:
        raise Exception("❌ Could not connect to Kafka after multiple retries")

def publish_event(producer, kafka_topic: str, event, metrics_published_success, metrics_published_error) -> None:
    try:
        logger.info(f"sending metric for {event['pod']}")
        producer.produce(kafka_topic, value=json.dumps(event).encode("utf-8"))
        producer.flush()
        logger.info("metric event sent to kafka topic")
        metrics_published_success.inc()
    except Exception as e:
        logger.info(f"a problem occurred while sending an event to kafka: {e}")
        metrics_published_error.inc()
