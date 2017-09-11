# coding:utf8
'''
Simple Logging Service
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))
from config import CONFIG
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file = '%s/root.log' % CONFIG['log_path']
print('Saving logs into', log_file)

fh = logging.FileHandler(log_file)
fh.setFormatter(formatter)
fh.setLevel(CONFIG['log_level'])
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(CONFIG['log_level'])

def getLogger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":
    logger = getLogger('foo')
    logger.info('bar')