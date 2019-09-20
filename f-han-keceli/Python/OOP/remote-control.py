#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:52:28 2019

@author: han
"""

import random
import time

class RemoteControl():
    
    def __init__(self,tv_status = "Off", tv_volume = 0, channel_list = ["NHK"], channel = "NHK"):
        
        
        self.tv_status = tv_status
        
        self.tv_volume = tv_volume
        
        self.channel_list = channel_list
        
        self.channel = channel
        
    
    def turnOn_tv(self):
        
        if(self.tv_status == "ON"):
            print("TV is already ON!")
        else:
            print("TV is opening..")
            self.tv_status = "ON"
            
    
    def turnOff_tv(self):
        if(self.tv_status == "OFF"):
            print("TV is already OFF!")
        else:
            print("TV is closing..")
            self.tv_status = "OFF"
            
            
    def adjustVolume(self):
        while True:
            answer = input("Decrease volume: '<'\nIncrease volume: '>'Exit: exit")
            
            if(answer == '<'):
                if(self.tv_volume != 0):
                    
                    self.tv_volume -= -1
                    print("Volume:",self.tv_volume)
            elif (answer == '>'):
                if(self.tv_volume != 32):
                    
                    self.tv_volume += 1
                        
                    print("Volume:", self.tv_volume)
                        
            else:
                print("Volume updated:",self.tv_volume)
                break
            
    def addChannel(self,channel_name):
        
        print("Channel adding..")
        time.sleep(1)
        
        self.channel_list.append(channel_name)
        
        print("Channel added.")
        
        
    def randomChannel(self):
        randomGenerate = random.randint(0,len(self.channel_list) -1)
        
        self.channel = self.channel_list[randomGenerate]
        
        print("Current channel:",self.channel)
        
        
    def __len__(self):
        
        return len(self.channel_list)
    
    def __str__(self):
        return "TV status: {}\nTv volume: {}\nChannel List: {}\nCurrent channel: {}\n".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)
    


remote = RemoteControl()
    
print("""
      
TV Application

1- Open TV

2- Close TV

3- Volume Settings

4- Add channel

5- Get number of channel

6- Change channel randomly

7- TV infos

q for exit 
""")

while True:
    process = input("Select Process: ")
    
    if(process == "q"):
        print("Program is closing...")
        time.sleep(1)
        break
    elif (process == 1):
        remote.turnOn_tv()
    elif(process == 2):
        remote.turnOff_tv()
    elif(process == 3):
        remote.adjustVolume()
    elif(process == 4):
        channel_names= input("Input channel names with ',' seperator")
        
        channel_list = channel_names.split(",")
        
        for addingChannels in channel_list:
            remote.addChannel(addingChannels)
    elif(process == 5):
        print("Number of channel:",len(remote))
        
    elif(process == 6):
        remote.randomChannel()
        
    elif(process == 7):
        print(remote)
        
    else:
        print("Invalid")