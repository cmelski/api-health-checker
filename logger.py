import logging


class Logger:

    def __init__(self):
        self.logger = self.get_logger_config()

    def get_logger_config(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )
        logger = logging.getLogger(__name__)
        return logger
