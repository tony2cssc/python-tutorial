#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def char2num(aChar):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[aChar]

def str2float(s):
    if not isinstance(s, str):
        raise TypeError('bad operand type. Here str is expected.')
    tempList = s.split(".")
    firstPart = reduce(lambda x, y: x * 10 + y, map(char2num, tempList[0] + tempList[1]))
    secondPart = firstPart * 10 ** -len(tempList[1])
    return secondPart

print('str2float(\'123.456789\') =', str2float('123.456789'))
