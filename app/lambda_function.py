import logging
import src.get_info as info

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info(f'Event: {event}')

    data = info.get_instance_info()

    response = {'Data:': data}
    logger.info(f'Data: {event}')

    return response
