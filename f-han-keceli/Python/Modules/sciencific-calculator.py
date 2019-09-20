#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:10:28 2019

@author: han
"""

import math
import time
 
print("""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Gelişmiş Hesap Makinesi
 
Lütfen Yapmak İstediğiniz İşlemin Numarısını Giriniz:
 
1-Toplama
2-Çıkartma
3-Çarpma
4-Bölme
5-Logaritma(Onluk tabanda)
6-Faktoriyel bulma
7-Kuvvet alma
8-Trigonometrik değerler
 
Çıkmak için 'q' karakterini giriniz.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
""")
def toplama(sayı1,sayı2):
    return sayı1 + sayı2
def çıkarma(sayı1,sayı2):
    return sayı1 - sayı2
def çarpma(sayı1,sayı2):
    return sayı1*sayı2
def bölme(sayı1,sayı2):
    return sayı1/sayı2
 
 
while True:
 
    işlem = input("İşlem Numarasını Giriniz:")
 
    if işlem == "q":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Yeniden Bekleriz")
        break
    elif işlem == "1":
        print("Toplamak istediğiniz sayıları giriniz.")
        sayı1 = int(input("Sayı1:"))
        sayı2 = int(input("Sayı2:"))
        time.sleep(1)
        print("{}+{}={}".format(sayı1,sayı2,toplama(sayı1,sayı2)))
    elif işlem == "2":
        print("Çıkarmak istediğiniz sayıları giriniz.")
        sayı1 = int(input("Sayı1:"))
        sayı2 = int(input("Sayı2:"))
        time.sleep(1)
        print("{}-{}={}".format(sayı1,sayı2,çıkarma(sayı1,sayı2)))
    elif işlem == "3":
        print("Çarpmak istediğiniz sayıları giriniz.")
        sayı1 = int(input("Sayı1:"))
        sayı2 = int(input("Sayı2:"))
        time.sleep(1)
        print("{}x{}={}".format(sayı1,sayı2,çarpma(sayı1,sayı2)))
    elif işlem == "4":
        print("Bölmek istediğiniz sayıları giriniz.")
        sayı1 = int(input("Sayı1:"))
        sayı2 = int(input("Sayı2:"))
        time.sleep(1)
        print("{}/{}={}".format(sayı1,sayı2,bölme(sayı1,sayı2)))
    elif işlem == "5":
        sayı1 = int(input("Logaritmasını almak istediğiniz sayıyı giriniz:"))
        time.sleep(1)
        print("log{} = {}".format(sayı1,math.log10(sayı1)))
    elif işlem == "6":
        sayı1 = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz:"))
        time.sleep(1)
        print("{}! = {}".format(sayı1,math.factorial(sayı1)))
    elif işlem == "7":
        sayı1 = int(input("Kuvvetini almak istediğiniz sayıyı giriniz:"))
        sayı2 = int(input("{} sayısının kaçıncı kuvvetinin alınacağını giriniz:".format(sayı1)))
        time.sleep(1)
        print("{} sayısının {}. kuvveti {} dir.".format(sayı1,sayı2,math.pow(sayı1,sayı2)))
    elif işlem == "8":
        sayı1 = int(input("Trigonometrik değerlerini almak istediğiniz açıyı giriniz:"))
        time.sleep(1)
        print("Sin{} = {:.2f}".format(sayı1,math.sin(math.radians(sayı1))))
        print("Cos{} = {:.2f}".format(sayı1, math.cos(math.radians(sayı1))))
        print("Tan{} = {:.2f}".format(sayı1, math.tan(math.radians(sayı1))))
        print("Cot{} = {:.2f}".format(sayı1,1 / math.tan(math.radians(sayı1))))
    else:
        print("Geçersiz işlem!")