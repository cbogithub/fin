#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
if(sys.version_info.major == 2):
    import ConfigParser as configparser
else:
    import configparser

class config:
    'config: read/write config file'

    def __init__(self, configFile='system.conf'):
        self.__file   = configFile
        self.__parser = configparser.SafeConfigParser()
        self.__parser.read(self.__file)

    def sections(self):
        return self.__parser.sections()

    def options(self, section):
        return self.__parser.options(section)

    def items(self, section):
        return self.__parser.items(section)

    def get(self, section, option):
        return self.__parser.get(section, option)

    def getint(self, section, option):
        return self.__parser.getint(section, option)

    def getfloat(self, section, option):
        return self.__parser.getfloat(section, option)		

    def getboolean(self, section, option):
        return self.__parser.getboolean(section, option)
		
    def addSection(self, section):
        self.__parser.add_section(section)
        self.__parser.write(open(self.__file, "w"))		

    def removeSection(self, section):
        self.__parser.remove_section(section)
        self.__parser.write(open(self.__file, "w"))	

    def removeOption(self, section, option):
        self.__parser.remove_option(section, option)
        self.__parser.write(open(self.__file, "w"))		
		
    def set(self, section, option, value):
        self.__parser.set(section, option, value)		
        self.__parser.write(open(self.__file, "w"))

