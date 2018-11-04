import config as cfg
import os
import logging


logger = logging.getLogger('bt-auto-downloader')
formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d] %(message)s', '%m-%d %H:%M:%S')

if cfg.dev_mode:
    logger.setLevel(logging.DEBUG)

    output = logging.StreamHandler()
    output.setLevel(logging.DEBUG)
    output.setFormatter(formatter)
    logger.addHandler(output)

else:
    logger.setLevel(logging.INFO)

    log_info = logging.FileHandler('info.log')
    log_info.setLevel(logging.INFO)
    log_info.setFormatter(formatter)
    logger.addHandler(log_info)

    log_error = logging.FileHandler('ERROR.log')
    log_error.setLevel(logging.WARN)
    log_error.setFormatter(formatter)
    logger.addHandler(log_error)

