#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:03:59 2019

@author: han
"""

import random
import time
 
print("""
**********************
NUMBER GUESSING GAME


GUESS NUMBER BETWEEN 1 AND 40
 
**********************
""")
random_number = random.randint(1,40)
guess_count = 7
counter = 0
 
while True:
    tahmin = int(input("Tahmininiz:"))
 
    if(tahmin < random_number):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin..")
        guess_count -= 1
        counter +=1
 
    elif(tahmin > random_number):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı giriniz..")
        guess_count -= 1
        counter += 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayımız:",random_number)
        print("Tahmin sayınız:",counter )
        break
    if(guess_count == 0):
        print("Tahmin Hakkınız Bitti!")
        print("Sayımız:",random_number)
        break