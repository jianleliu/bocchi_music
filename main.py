import sys

# this has to be instantiated before any widgets instance.
from app import app
from ui.MainWindow import MainWindow
from datetime import datetime
import logging
import os

logger = logging.getLogger(__name__)

def configure_logger():
    format = '%(asctime)s | %(levelname)s | %(filename)s - %(funcName)s - %(message)s'
    dir_log = os.path.join(os.getcwd(), 'log')
    log_filename = os.path.join(dir_log, f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log')
    
    
    if not os.path.isdir(dir_log):
      os.mkdir(dir_log)
    logging.basicConfig(filename=log_filename, format=format, level=logging.INFO)
    logger.info('logger configured')


def main():
    window = MainWindow()
    logger.info('initializing MainWindow successful')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    configure_logger()
    logger.info('initializing MainWindow')
    main()
    
