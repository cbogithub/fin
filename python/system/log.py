#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

class log:
    'log: log with console and file'
    DEBUG    = logging.DEBUG
    INFO     = logging.INFO	
    WARNING  = logging.WARNING 
    ERROR    = logging.ERROR 
    CRITICAL = logging.CRITICAL

    FORMAT_DATA     = '%(message)s'
    FORMAT_LEVEL    = '%(asctime)s - %(levelname)s - %(message)s'
    FORMAT_RELATIVE = '%(relativeCreated)s - %(levelname)s - %(message)s'	
    FORMAT_FUNC     = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d; %(module)s:%(funcName)s()] - %(message)s'
    FORMAT_LOGGER   = '%(asctime)s - [%(name)s] - %(message)s'

    def __init__(self, name='log', level=DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.streams = {}
        self.setStream(level=self.DEBUG, format=self.FORMAT_FUNC)

    def setStream(self, filename='', level=None, format=None):
        if(filename in self.streams):
            newstream = self.streams[filename];

        else:
            if(filename == ''):
                newstream = logging.StreamHandler() 
            else:
                newstream = logging.FileHandler(filename)
            if(level == None):
                level = self.INFO
            if(format == None):
                format = self.FORMAT_LEVEL
            
        if(level != None):
            newstream.setLevel(level)
        if(format != None):
            newstream.setFormatter(logging.Formatter(format))                
        self.streams[filename] = newstream
        self.logger.addHandler(newstream)
		
    def removeStream(self, filename=''):
        delstream = self.streams.pop(filename)
        self.logger.removeHandler(delstream)
        del self.streams[filename]
		
    def debug(self, content):
        self.logger.debug(content)

    def info(self, content):
        self.logger.info(content)

    def warning(self, content):
        self.logger.warning(content)
		
    def error(self, content):
        self.logger.error(content)

    def critical(self, content):
        self.logger.critical(content)


class scopelog:
    'scopelog: log with enter and exit scope block'
    __depth = 0
	
    def __init__(self, name='scopelog', level=log.DEBUG):
        self.logger = log(name, level)
        self.logger.setStream(level=log.DEBUG, format=log.FORMAT_LOGGER)
        scopelog.__depth +=1
        self.__log('Enter (%d)' % scopelog.__depth)

    def __del__(self):
        self.__log('Exit (%d)' % scopelog.__depth)
        scopelog.__depth -=1		
		
    def __log(self, content):
	    self.logger.debug(content)
		
    def depth():
        return scopelog.__depth
