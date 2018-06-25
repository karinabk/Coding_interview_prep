#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:11:23 2018

@author: karina
"""

def quickSort(list_):
    helper(0,len(list_)-1,list_)
    
    
def helper(index_lo,index_hi,list_):
    if index_lo > index_hi:
        return
    left = index_lo
    right = index_hi
    pivot =list_[index_lo]
    while True:        
        while list_[index_hi]>pivot:
            index_hi-=1
        while list_[index_lo]<pivot:
            index_lo+=1
        temp = list_[index_lo]
        list_[index_lo]=list_[index_hi]
        list_[index_hi]=temp
        if index_hi >= index_lo: break
    
    helper(index_lo + 1, right,list_)
    helper(left, index_hi - 1, list_)
    
    
    
if __name__=="__main__":
    a = [3,2,11,3,22, 0]
    quickSort(a)
    print(a)