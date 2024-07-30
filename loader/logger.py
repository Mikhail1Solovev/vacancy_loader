import logging

class Logger:
    @staticmethod
    def setup_logging(log_file='vacancy_loader.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
