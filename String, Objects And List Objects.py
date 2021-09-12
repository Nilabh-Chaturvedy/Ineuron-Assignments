# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:43:42 2021

@author: nchaturvedy

Python Assignment : String, Objects And List Objects
"""
#Question 1
for i in range(1,5):
     for j in range(1,i+1):
        print("*",end='')
     print('\n')
for i in range(5,0,-1):
     for j in range(1,i+1):
        print("*",end='')
     print('\n')    

#Question 2

def reverse(word):
    return word[::-1]

def main():
    print("please enter a word")
    wrd=input()
    print("the reversed word is :",reverse(wrd))

main()