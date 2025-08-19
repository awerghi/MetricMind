from db.models.alert_model import AlertModel
from db.session.db_handler import session


def get_db ():
    db = session()
    try:
        return db
    finally:
        db.close()

def push_alert_to_db (db,alert_record):
    alert_record_model = AlertModel(
        cluster= alert_record['cluster'],
        timestamp=alert_record['timestamp'],
        node_identifier=alert_record['node'],
        pod_identifier=alert_record['pod'],
        cpu_usage=alert_record['cpu'],
        memory_usage=alert_record['memory'],
        investigation_decision=alert_record['investigation_decision'],
        alert_level=alert_record['pod_alert_level'].upper(),
        troubleshooting_steps = alert_record['troubleshooting_steps'])

    db.add(alert_record_model)
    db.commit()
