#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:18:19 2018

@author: karina
"""

def bubbleSort(mylist):
    for j in mylist:
        for i in range(len(mylist)-1):
            if mylist[i]>mylist[i+1]:
                teemp = mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1]=teemp
    return mylist
    
    
if __name__=="__main__":
    list_ = [1,3,5,2,10,0]
    print(bubbleSort(list_))
    