from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Global settings
    JOB_NAME : str = "agent-metrics-job"
    NUMBER_OF_THREADS : int = 4

    # kafka connection retries
    NUMBER_OF_RETRIES : int = 10
    KAFKA_TOPIC : str = "agent-metrics-prod"



app_settings = Settings()
