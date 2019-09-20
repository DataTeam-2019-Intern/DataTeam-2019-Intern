#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:01:35 2019

@author: han
"""

class Folder():
    
    def __init__(self):
        
        with open("text.txt","r",encoding="utf-8") as file:
            
            folder_content = file.read()
            self.just_words  = list()
            
            words = folder_content.split()
            
            for i in words:
                print(i)
                
                i = i.strip("\n")
                
                i = i.strip(".")
                
                i = i.strip(",")
                
                self.just_words.append(i)
    
                
    def all_words(self):
        
        words_set = set()
        
        for i in self.just_words:
            words_set.add(i)
            
        print("All Words -------")
        
        for i in words_set:
            
            print(i)
            
            print("****************")
            # print(folder_content)
            
    def word_frequency(self):
        
        word_dict = dict()
        
        for i in self.just_words:
            
            if(i in word_dict):
                word_dict[i] += 1
                
            else:
                word_dict[i] = 1
        
        for word,number in word_dict.items():
            
            print("{} words iterating {} times..".format(word,number))
            
            print("-----------------------------------")
             
folder = Folder()

#folder.all_words()

folder.word_frequency()
