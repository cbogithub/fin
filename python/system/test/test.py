#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system import log, config

'''
log test
'''
loger=log.getStreamLogger("test", log.DEBUG)
loger=log.getFileLogger("test", "system/test/test.log", log.DEBUG)

loger.debug('============= test log ========')
loger.debug('debug')
loger.info('info')
loger.warning('warning')
loger.error('error')
loger.critical('critical')

loger1=log.scopelog("LOGER1")
loger2=log.scopelog("LOGER2")
del loger2
del loger1

loger.debug('============= config test ========')
configer=config("system/test/test.conf")


configer.removeSection("system")
configer.addSection("system")
configer.set("system", "key1", "value1")
configer.set("system", "key2", "12345")
loger.debug(configer.get("system", "key1"))
loger.debug(configer.getint("system", "key2"))

loger.debug('============= end test ========')

