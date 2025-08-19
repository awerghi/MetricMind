from sqlalchemy import Column, INTEGER, String, TIMESTAMP

from db.session.db_handler import Base

class AlertModel(Base):

    __tablename__ = "pod_alerts"

    id = Column(INTEGER,primary_key=True,autoincrement=True)
    cluster = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    node_identifier = Column(String)
    pod_identifier = Column(String)
    cpu_usage = Column(String)
    memory_usage = Column(String)
    investigation_decision = Column(String)
    alert_level = Column(String)
    troubleshooting_steps = Column(String)