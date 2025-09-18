import os
import logging

class LogGen:
    @staticmethod
    def loggen():
        log_directory = '.\\Logs'
        log_file = 'automation.log'
        log_path = os.path.join(log_directory, log_file)

        # Create Logs directory if it does not exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Create logger
        logger = logging.getLogger('AutomationLogger')
        logger.setLevel(logging.INFO)

        # Clear existing handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        # File handler
        file_handler = logging.FileHandler(log_path, mode='a')
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                           datefmt='%d-%b-%y %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                              datefmt='%H:%M:%S')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        return logger
