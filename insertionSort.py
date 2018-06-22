#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:18:19 2018

@author: karina
"""

def insertionSort(mylist):
    for j in range(len(mylist)):
        for i in range(j):
            if j-i-1<0:
                break
            if mylist[j-i-1]>mylist[j-i]:
                teemp = mylist[j-i]
                mylist[j-i]=mylist[j-i-1]
                mylist[j-i-1]=teemp
    return mylist
    
    
if __name__=="__main__":
    list_ = [3,3,444,5,3,1,0,34,5,7]
    print(insertionSort(list_))
    