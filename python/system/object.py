#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from . import log

class VALUE:
    def __init__(self, value=None):
        if(value == None):
            self.__exist   = False
        else:
            self.__exist   = True
            self.__value   = value
            
    def exist(self):
        return self.__exist
        
    def get(self):
        if(not self.exist()):
            raise log.crash("value NOT exist!")
            return None
        return self.__value
    
    def set(self, value):
        self.__value = value
        return True

        
class callback:
    def __init__(self, run=None):
        self.timeStat = statistics()
        if(run == None):
            self.__exist   = False
        else:
            self.__exist   = True
            self.__run     = run

    def exist(self):
        return self.__exist
        
    def run(self, *a):
        if(not self.exist()):
            raise log.crash("callback function NOT exist!")
        startTime = time.time()
        ret = self.__run(*a)
        self.timeStat.read(int(round((time.time()-startTime) * 1000)))
        log.getLogger("object.callback").debug("run %s with %d ms" % (self.__run.__name__, self.timeStat.last()))
        return ret 


        
class statistics:
    def __init__(self):
        self.values = []

    def read(self, value):
        self.values.append(value)
    

    def first(self):
        return self.values[0]
    def last(self):
        return self.values[-1]
    def min(self):
        return min(self.values)
    def max(self):
        return max(self.values)
    def len(self):
        return len(self.values)        
    def total(self):
        value = 0
        for i  in self.values:
            value += self.values[i]
        return value
    def average(self):
        return self.total()/self.len()
