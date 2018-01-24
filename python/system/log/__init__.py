#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
          'FORMAT_DATA', 'FORMAT_LEVEL', 'FORMAT_RELATIVE', 'FORMAT_FUNC', 'FORMAT_LOGGER',
          'getLogger', 'getStreamLogger', 'getFileLogger', 'scopelog']

import logging

DEBUG    = logging.DEBUG
INFO     = logging.INFO	
WARNING  = logging.WARNING 
ERROR    = logging.ERROR 
CRITICAL = logging.CRITICAL

FORMAT_DATA     = '%(message)s'
FORMAT_LEVEL    = '%(asctime)s - %(levelname)s - %(message)s'
FORMAT_RELATIVE = '%(relativeCreated)s - %(levelname)s - %(message)s'	
FORMAT_FUNC     = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d; %(module)s:%(funcName)s()] - %(message)s'
FORMAT_LOGGER   = '%(asctime)s - %(levelname)s - [%(name)s] - %(message)s'

def getLogger(module='log', file='', level=None, format=None):
    if( file == '' ):
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(file)

    if( level != None):
        handler.setLevel(level)
    if( format != None):
        handler.setFormatter(logging.Formatter(format))

    logger = logging.getLogger(module)

    if( level != None):
        logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def getStreamLogger(module='log', level=DEBUG, format=FORMAT_FUNC):
    return getLogger(module, '', level, format)
    
def getFileLogger(module='log', file='log/log.log', level=INFO, format=FORMAT_LOGGER):
    return getLogger(module, file, level, format)

class scopelog:
    'scopelog: log with enter and exit scope block'
    __depth = 0
	
    def __init__(self, module='scopelog', file='', level=DEBUG, format=FORMAT_LOGGER):
        self.logger = getLogger(module, file, level, format)
        scopelog.__depth +=1
        self.__log('Enter (%d)' % scopelog.__depth)

    def __del__(self):
        self.__log('Exit (%d)' % scopelog.__depth)
        scopelog.__depth -=1		
		
    def __log(self, content):
	    self.logger.debug(content)
		
    def depth():
        return scopelog.__depth

class crash(ValueError):
    pass
