from logging import getLogger, FileHandler, Formatter, DEBUG


handler = FileHandler(filename="logger.log")
handler.setLevel(DEBUG)
handler.setFormatter(Formatter("%(asctime)s %(levelname)8s %(name)s %(message)s"))

logger = getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(handler)



if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
