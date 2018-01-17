#!/bin/sh

PYTHONPATH=`pwd` python2.7 system/test/test.py
PYTHONPATH=`pwd` python2.7 finance/exchangeAgent/test/test.py

