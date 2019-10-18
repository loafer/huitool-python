import logging
import sys
from huitool.logging import settings as logging_settings


def main():
    print(sys.path)

    logging_settings.configure(logging_config_file='.\\tests\logging.yaml')
    # logging_settings.configure(extra={'app':'python'})
    # logging_settings.configure(logging_file='python.log.json', extra={'app':'python'})
    

    logger = logging.getLogger(__name__)
    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')

    # adapter = CustomAdapter(logger, {'app': 'python'})
    # adapter.info('adapter info')

    try:
        5/0
    except Exception:
        logger.exception('exception')

if __name__ == "__main__":
    main()         