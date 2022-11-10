import logging
import sys

from app.setting import settings
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


class Logger:
    def __init__(self, level: str):
        self.log_path = Path(settings.log_path)
        self.log_path.mkdir(parents=True, exist_ok=True)
        self.level = level
        self.logger = logging.getLogger(level)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler = logging.StreamHandler(sys.stdout)
        fhandler = TimedRotatingFileHandler(
            filename=self.log_path / ".log",
            when="D",
            backupCount=100,
            encoding="utf-8",
            delay=True
        )
        fhandler.suffix = "%Y-%m-%d"
        handler.setFormatter(formatter)
        fhandler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.addHandler(fhandler)

    def info(self, str: str):
        self.logger.info(
            f"""{str}"""
        )

    def error(self, str: str):
        self.logger.error(
            f"""{str}"""
        )

    def exception(self, str: str):
        self.logger.exception(
            f"""{str}"""
        )
