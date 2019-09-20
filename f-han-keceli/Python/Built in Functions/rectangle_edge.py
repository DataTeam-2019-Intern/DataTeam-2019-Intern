#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:41:33 2019

@author: han
"""

def calculate_area(Tuple):
    return Tuple[0] * Tuple[1]

List = [(3,4),(10,3),(5,6),(1,9)]

print((list(map(calculate_area,List))))