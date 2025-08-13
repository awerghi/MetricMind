import logging

from pathlib import Path


LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

def setup_logger():
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers = [
            logging.FileHandler(LOG_DIR / "app.log"),
            logging.StreamHandler()
        ],
        force=True
    )
    return logging.getLogger(__name__)

logger = setup_logger()

logger.info("First log message")  # This triggers file creation
