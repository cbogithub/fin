#!/bin/sh

echo "================ python2 test============="
PYTHONPATH=`pwd` python2.7 system/test/test.py
#PYTHONPATH=`pwd` python2.7 finance/exchangeAgent/test/test.py

echo "================ python3 test============="
PYTHONPATH=`pwd` python system/test/test.py

#TODO: open if ssl is not available
#PYTHONPATH=`pwd` python finance/exchangeAgent/test/test.py
