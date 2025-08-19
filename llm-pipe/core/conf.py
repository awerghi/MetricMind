from pydantic.v1 import BaseSettings


class Settings(BaseSettings):

    #Global settings
    JOB_NAME : str = "llm-pipe"

    # LLM settings
    Model_Version : str = "mistral-tiny"
    APP_OPERATION : str = """Analyze these metrics for"""
    PROMPT_FOCUS : str = """Provide insights focusing on:
                            1. issue_description
                            2. how to solve the issue"""
    LLM_NUMBER_RETRIES : int = 2

    # KAFKA
    NUMBER_OF_RETRIES : int = 3
    KAFKA_BOOTSTRAP_SERVERS : str = "kafka:29092"
    GROUP_ID : str = 'llm_consumer'
    ENABLE_AUTO_COMMIT : str = 'false'
    AUTO_OFFSET_RESET : str = 'latest'
    AGENT_METRICS_CRITICAL_PROD : str = "agent-metrics-critical-prod"
    EVENTS_THRESHOLD : int = 2

settings = Settings()