import logging.config

from utils.apple import eat_apple
from utils.pear import eat_pear

logging.config.fileConfig('logging.ini')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('I\'m craving fruit')
    eat_apple()
    eat_pear()
