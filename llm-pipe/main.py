import logging

from core.conf import settings
from db.utils.alerts_db_operations import get_db
from kafka.consumer import  connect_to_kafka, consume_event_prompt_llm
from db.models.alert_model import AlertModel


from db.session.db_handler import Base, database_engine

conf = {'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        'group.id': settings.GROUP_ID,
        'enable.auto.commit': settings.ENABLE_AUTO_COMMIT,
        'auto.offset.reset': settings.AUTO_OFFSET_RESET}

if __name__ == "__main__":
    try:
        db = get_db()
        Base.metadata.create_all(database_engine)
        consumer = connect_to_kafka(conf, settings.NUMBER_OF_RETRIES)
        llm_response = consume_event_prompt_llm(consumer, settings.AGENT_METRICS_CRITICAL_PROD, db)
    except Exception as e :
        logging.error("Cannot create table in database")

