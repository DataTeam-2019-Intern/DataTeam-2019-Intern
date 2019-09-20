#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:53:28 2019

@author: han
"""

from functools import reduce

List = [1,2,3,4,5,6,7,8,9,10]

Filter = list(filter(lambda x : x % 2 == 0, List))

print(reduce(lambda x,y : x + y,Filter))