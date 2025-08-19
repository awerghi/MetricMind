from pydantic import BaseModel, Field

class CriticalMetric(BaseModel):
    issue_description: str = Field(description="Give me a description that explains what is going on and why the metric"
                                               " is prioritized")
    investigation_decision : str = Field(description="the metrics should be investigated by the teams or not, "
                                                     "respond with YES or NO")
    pod_alert_level : str = Field(description="give the level of alert between low/medium/high")
    troubleshooting_steps : str = Field(description="brief troubleshooting steps with kubectl commands")

class CriticalMetricEvents(BaseModel):
    response : list[CriticalMetric]