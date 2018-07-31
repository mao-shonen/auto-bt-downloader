import os
import logging


DEV = os.environ.get('dev', False)


logger = logging.getLogger('RSSer')
logger.setLevel(logging.DEBUG) if DEV else logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d] %(message)s', '%m-%d %H:%M:%S')

log_file = logging.FileHandler('ERROR.log')
log_file.setLevel(logging.WARN)
log_file.setFormatter(formatter)
logger.addHandler(log_file)

output = logging.StreamHandler()
output.setLevel(logging.INFO) if DEV else logger.setLevel(logging.INFO)
output.setFormatter(formatter)
logger.addHandler(output)
