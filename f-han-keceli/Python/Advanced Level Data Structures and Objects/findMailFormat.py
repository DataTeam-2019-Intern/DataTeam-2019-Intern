#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:01:10 2019

@author: han
"""

with open("emails.txt","r",encoding="utf-8") as file:
    for row in file:
        row = row[:-1]
        if(row.endswith(".com") and row.find("@")!= -1):
            print(row)