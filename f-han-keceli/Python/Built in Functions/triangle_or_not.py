#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:46:11 2019

@author: han
"""

def triangle(Tuple):
    
    if (abs(Tuple[0]+Tuple[1]) > Tuple[2] and abs(Tuple[0]+Tuple[2]) > Tuple[1] and abs(Tuple[1]+Tuple[2]) > Tuple[0]):
        return True
    else:
        return False


liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(triangle,liste)))