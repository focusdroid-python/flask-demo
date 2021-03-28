import logging

# 设置日志输出样式
logging.basicConfig(
    level=logging.INFO,
    format='levelname:%(levelname)s filename: %(filename)s '
           'outputNumber: [%(lineno)d] thread: %(threadName)s output msg: %(message)s'
           ' - %(asctime)s ',
    datefmt='[%d/%b/%Y %:H%:M%S]'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('this is a info log')
    logger.info('this is a info log 1')
    logger.error('this is a error errorlog')
    logger.error('this is a error errorlog 1')