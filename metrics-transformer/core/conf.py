from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # the topic the job will listen to, this is where events are pushed
    METRICS_TOPIC : str = "agent-metrics-prod"
    # the name of the topic where we are going to send critical metrics to
    CRITICAL_METRICS_TO_HANDLE_TOPIC : str = "agent-metrics-critical-prod"
    # The value from where the metric is considered critical and should be handled
    METRICS_THRESHOLD : int = 7

settings = Settings()
