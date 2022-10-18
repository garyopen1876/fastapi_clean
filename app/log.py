import logging


class Loggers():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(filename='./server.log')
    formatter = logging.Formatter(
        "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
    )

    def file_write():
        Loggers.fh.setFormatter(Loggers.formatter)
        Loggers.logger.addHandler(Loggers.fh)

    def terminal_show():
        Loggers.ch.setFormatter(Loggers.formatter)
        Loggers.logger.addHandler(Loggers.ch)
    
    # level
    def debug(message):
        Loggers.logger.debug(message)
        Loggers.file_write()
        Loggers.terminal_show()

    def info(message):
        Loggers.logger.info(message)
        Loggers.file_write()
        Loggers.terminal_show()
    
    def warning(message):
        Loggers.logger.warning(message)
        Loggers.file_write()
        Loggers.terminal_show()
    
    def error(message):
        Loggers.logger.error(message)
        Loggers.file_write()
        Loggers.terminal_show()

    def critical(message):
        Loggers.logger.critical(message)
        Loggers.file_write()
        Loggers.terminal_show()

 
