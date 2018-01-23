#!/usr/bin/python
# -*- coding: utf-8 -*-


import math

def downRound(decimal, digits):
    return int(decimal * math.pow(10, digits)) / int(math.pow(10, digits))
