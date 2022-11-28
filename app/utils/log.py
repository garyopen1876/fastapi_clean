import logging
import sys
import requests

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

    def telegrem_call(self, str: str):
        apiURL = f'https://api.telegram.org/bot{settings.telegrem_api_token}/sendMessage'
        try:
            requests.post(
                apiURL, json={'chat_id': settings.telegrem_chat_id, 'text': str})
        except Exception as e:
            print(e)

    def info(self, str: str):
        self.telegrem_call(str)
        self.logger.info(
            f"""{str}"""
        )

    def error(self, str: str):
        self.telegrem_call(str)
        self.logger.error(
            f"""{str}"""
        )

    def exception(self, str: str):
        self.telegrem_call(str)
        self.logger.exception(
            f"""{str}"""
        )
