#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:34:15 2019

@author: han
"""

initial_letter = ""

with open("poet.txt","r",encoding="utf-8") as file:
    for row in file:
        initial_letter += row[0]

print(initial_letter)