import os

from quixstreams import Application

from core.conf import settings
from core.log import logger

bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS","kafka:29092")

app = Application(
    broker_address=bootstrap_servers,
)

metrics_topic = app.topic(settings.METRICS_TOPIC,value_deserializer="json")
priority_metrics = app.topic(settings.CRITICAL_METRICS_TO_HANDLE_TOPIC,value_serializer="json")

def pipeline (app):
    try:
        # Create a Streaming DataFrame connected to the metrics topic
        sdf = app.dataframe(topic=metrics_topic)

        # We will filter the kafka events where metric_priority is more than metrics_threshold
        filtered_sdf = (sdf.filter(lambda row: row['metric_priority'] > settings.METRICS_THRESHOLD))

        # send filtered events to a new topic
        logger.info(f"event dispatched from {settings.METRICS_TOPIC} to {settings.CRITICAL_METRICS_TO_HANDLE_TOPIC} ")
        filtered_sdf.to_topic(priority_metrics)

    except Exception as e:
        logger.error(f"Cannot dispatch events from {settings.METRICS_TOPIC} to {settings.CRITICAL_METRICS_TO_HANDLE_TOPIC} due to {e}")

if __name__ == "__main__":
    pipeline(app)
    app.run()