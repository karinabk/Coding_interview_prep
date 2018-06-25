#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:11:23 2018

@author: karina
"""
def swap(index1,index2,list_):
    temp = list_[index1]
    list_[index1]=list_[index2]
    list_[index2]=temp
    
def selectionSort(list_):
    
    for j in range(len(list_)):
        minV = list_[j]
        indexMin=j
        for i in range(len(list_)-j):
            if minV>list_[i+j]:
                minV=list_[i+j]
                indexMin=i+j
        swap(j,indexMin,list_)
            
 
    
    
    
if __name__=="__main__":
    
    a = [3,2,11,44,3,2,1,2,3,4444,444444444444,3,22, 0]
#    print(a)
    selectionSort(a)
#    print(a)