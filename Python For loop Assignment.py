# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:51:11 2021

@author: nchaturvedy

PYTHON BASIC Assignment questions
"""



 #Question 1 
for i in range(2000,3201):
    if i%5!=0 and i%7==0:
         print(i,",")
    else : 
        continue
        
    

#Question 2
def reverse_name(f,s):
    print("the reversed name is " ,f[::-1]," ",s[::-1])
    
def main():
    print("Please enter your first name")
    first_name=input()
    print("Please enter your second name")
    second_name=input()
    reverse_name(first_name,second_name)
    
main()

#Question 3
def vol_spehere(d):
    pi=3.14
    v=4/3*pi*(d/2)**3
    return v
def main_2():
    print("please enter the diameter of the sphere")
    D=float(input())
    print(" the volume of the sphere is {} cubic units".format(vol_spehere(D)))
    
main_2()