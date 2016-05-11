# coding: utf-8

import logging, logging.handlers

def setLogger(logger_name = 'public', filename = 'log/public/public.log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    handler = logging.handlers.WatchedFileHandler(filename)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger 

def getPublicLogger():
    return logging.getLogger('public')

