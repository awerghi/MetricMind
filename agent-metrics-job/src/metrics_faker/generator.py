import random
from datetime import datetime,timezone

from  faker import Faker


fake = Faker()

# fake event
def generate_metric_event():
    return {
    "timestamp": str(datetime.now(timezone.utc)),
    "namespace": f"{fake.word()}-{fake.word()}",
    "pod": f"pod-{fake.uuid4()}",
    "cpu":  random.uniform(5.0,90.0),
    "memory": random.uniform(1.0,16.0),
    "metric_priority" : int(random.uniform(1.0,10.0))
}