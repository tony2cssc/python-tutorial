#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print("by Name: ")
print(L2)

L3 = sorted(L, key=by_score, reverse=True)
print("By score:")
print(L3)
