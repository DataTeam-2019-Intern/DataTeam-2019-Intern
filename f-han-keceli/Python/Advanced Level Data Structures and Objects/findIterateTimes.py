#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:27:13 2019

@author: han
"""

string = "ProgrammingCodeofAdvancedLevelDataStructuresandOnjectsipynb"

frequency = dict()

for char in string:
    if(char in frequency):
        frequency[char] += 1
    else:
        frequency[char] = 1
        
for i,j in frequency.items():
    
    print(i,":",j)