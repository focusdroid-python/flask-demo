# -*- coding:utf-8 -*-

import logging

logging.basicConfig(level=logging.INFO,
                    format='levelname:%(levelname)s filename: %(filename)s',
                    datefmt='%a %d %b %Y %H:%M:%S', filename='./my.log', filemode='w')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('this is info log')
    logger.warning('this. is warning log')
    logger.error('this is error log')
    logger.debug('this is debug log')