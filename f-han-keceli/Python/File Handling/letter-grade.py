#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:26:28 2019

@author: han
"""

def calculate_grade(row):
    
    row = row[:-1]
    
    List = row.split(",")
    
    name = List[0]
    
    grade1 = int(List[1])
    
    grade2 = int(List[2])
    
    grade3 = int(List[3])
    
    final_grade = grade1*0.3 + grade2 * 0.3 + grade3 *0.4
    
    if(final_grade >= 90):
        letter = "AA"
        
    elif(final_grade >= 85):
        letter = "BA"
        
    elif(final_grade >= 80):
        letter = "BB"
    
    elif(final_grade >= 75):
        letter = "CB"
    
    elif(final_grade >= 70):
        letter = "CC"
    
    elif(final_grade >= 65):
        letter = "DC"
        
    elif(final_grade >= 60):
        letter = "DD"
        
    elif(final_grade > 55):
        letter = "FD"
    
    else:
        letter = "FF"
        
    
    return name + "----------------" + letter + "\n"
    
        


with open("folder.txt","r",encoding= "utf-8") as file:
    
    addingList = []
    for i in file:
        addingList.append(calculate_grade(i))
        
    with open("grades.txt","w",encoding= "utf-8") as file2:
        for i in addingList:
            file2.write(i)
            
    with open ("failed.txt", "w", encoding="utf-8") as file3:
        for i in addingList:
            if "FF" in i:
                file3.write(i)
                pass
            
            elif "FD" in i:
                file3.write(i)
                pass
            
    with open("passed.txt", "w", encoding="utf-8") as file4:
        for i in addingList:
            if "FF" not in i:
                file4.write(i)
                pass
            elif "FD" not in i:
                file4.write(i)
                pass
            
    print(addingList)