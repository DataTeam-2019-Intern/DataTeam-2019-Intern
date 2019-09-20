#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:18:46 2019

@author: han
"""

names = ["Al","Gerald","Bessie","Rufus","Leland","Gladys"]

surnames = ["Lee","Hardy","Sparks","Hansen","Edwards","Wilkins"]

List = list(zip(names,surnames))

List.sort()

for i,j in List:
    print(i,j)