#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:11:02 2019

@author: han
"""

with open("footballers.txt","r",encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()
    
    for row in file:
        row = row[:-1]
        row_elements = row.split(",")
        if (row_elements[1] == "Fenerbahce"):
            fb.append(row + "\n")
        elif(row_elements[1] == "Galatasaray"):
            gs.append(row + "\n")
            
        else:
            bjk.append(row + "\n")
    
    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
            
    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
            
    with open("bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)
        
            