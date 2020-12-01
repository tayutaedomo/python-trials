"""
    Reference:
        - https://srbrnote.work/archives/5225
        - https://docs.python.org/ja/3/library/logging.handlers.html?highlight=logging%20handler#timedrotatingfilehandler
"""
from logging import getLogger, Formatter, DEBUG
from logging.handlers import TimedRotatingFileHandler


handler = TimedRotatingFileHandler(
    'logger_rotate.log',
    encoding='utf-8',
    when='S',
    interval=5,
    backupCount=5,
)
handler.setLevel(DEBUG)
handler.setFormatter(Formatter("%(asctime)s %(levelname)8s %(name)s %(message)s"))

logger = getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(handler)



if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
