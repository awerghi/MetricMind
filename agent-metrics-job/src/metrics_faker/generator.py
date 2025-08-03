import random
from  faker import Faker


fake = Faker()

# fake event
def generate_metric_event():
    return {
        "agent_id" : f"agent-{fake.uuid4()}",
        "metric_priority" : round(random.uniform(0,10)),
        "metric_source": {
            "host": "prod-checkout-web-05",
            "datacenter": f"aws-us-east-{fake.uuid4()}",
            "service": f"{random.choice(['back','front','ops'])}-service",
            "responsible_email": fake.email()
        },
        "metrics" : {
            "cpu_usage" : random.uniform(5.0,90.0),
            "memory_usage_gb" : random.uniform(1.0,16.0)},

            "context": {
                "service" : random.choice(["prod","stage","dev"]),
                "business_owner" : random.choice(["backend","frontend","ops"]),
                "cost_per_hour" : random.uniform(0,2),
                "baseline_cpu" : int(random.uniform(5.0,60.0)),
                "sla_threshold" : int(random.uniform(80,99))
            }
    }