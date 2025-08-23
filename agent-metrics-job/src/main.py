import os
import threading
import time


from prometheus_client import CollectorRegistry, push_to_gateway

from kafka_tools.publisher import connect_to_kafka,publish_event
from metrics_faker.generator import generate_metric_event
from metrics_faker.tracking_metrics import generated_events,fake_metrics_published_success,fake_metrics_published_error
from conf.settings import app_settings


registry = CollectorRegistry()
bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS","kafka:29092")
fake_metrics_event_numbers = generated_events(registry)
metrics_published_success = fake_metrics_published_success(registry)
metrics_published_error = fake_metrics_published_error(registry)

def pipeline_process():
    # the idea is to set a job that sends metrics all the time in order to simulate a production environment
    while True:
        producer = connect_to_kafka(bootstrap_servers,app_settings.NUMBER_OF_RETRIES)
        fake_metric = generate_metric_event()
        fake_metrics_event_numbers.inc()
        publish_event(producer, app_settings.KAFKA_TOPIC,event=fake_metric,metrics_published_success=metrics_published_success,
                      metrics_published_error=metrics_published_error)
        push_to_gateway("pushgateway:9091",job=app_settings.JOB_NAME,registry=registry)
        time.sleep(10)

threads = []
for i in range(app_settings.NUMBER_OF_THREADS):
    th = threading.Thread(target=pipeline_process)
    threads.append(th)
    th.start()

for th in threads:
    th.join()





