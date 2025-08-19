import time
import logging


from confluent_kafka import Consumer, KafkaException

from llm.prompt import prompt_llm_with_retry
from core.conf import settings

logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers= [
        logging.StreamHandler()
    ]
)

def connect_to_kafka(conf, number_of_retries: int):
    for attempt in range(number_of_retries):
        try:
            consumer = Consumer(conf)
            logging.info("✅ Connected to Kafka")
            return consumer
        except Exception as e:
            logging.info(f"⏳ Kafka not ready yet, retrying... {e}")
            time.sleep(5)
    else:
        raise Exception("❌ Could not connect to Kafka after multiple retries")

def consume_event_prompt_llm(consumer, kafka_topic: str,db):
    try:
        consumer.subscribe([kafka_topic])
        # llm will be prompted after a defined size of events
        event_count = 0
        events = []
        while True:

            try:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if event_count > settings.EVENTS_THRESHOLD:
                    prompt_llm_with_retry(db,events,settings.APP_OPERATION,settings.PROMPT_FOCUS,settings.LLM_NUMBER_RETRIES)
                    event_count = 0
                    events = []
                else:
                    event_count += 1
                    events.append(msg)
                    logging.info(events)

            except KafkaException as ke:
                logging.error(f"Kafka exception while consuming event: {ke}")
                time.sleep(5)
    except Exception as e:
        logging.error(f"Unexpected error while consuming event: {e}")
        raise
    finally:
        try:
            consumer.close()
        except Exception as e:
            logging.error(f"Error closing consumer: {e}")
