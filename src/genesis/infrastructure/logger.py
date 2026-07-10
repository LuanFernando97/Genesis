import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
SIMULATION_ID = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logger_levels = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "notset": logging.NOTSET,
}


def _create_logger(name: str, level: int, format_str: str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    logger_path = LOG_DIR / f"{SIMULATION_ID}"
    logger_path.mkdir(exist_ok=True)

    log_file = logger_path / f"{name}.log"
    logger = logging.getLogger(name)

    format = (
        format_str
        if format_str
        else "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    formatter = logging.Formatter(format)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_logger(
    name: str, level: str = "info", format_str: str = None
) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger = _create_logger(name, logger_levels[level], format_str)
    return logger
