#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:18:19 2018

@author: karina
"""

def mergeSort(mylist):
    
    if len(mylist)==1:
        return mylist
    
    list2=[]
    temp = len(mylist)
    while len(mylist) != int(temp/2):
        list2.append(mylist.pop())
  
    return merge(mergeSort(mylist),mergeSort(list2))
           
    
def merge(list1,list2):
    temp = []
    
    while len(list1)!=0 and len(list2)!=0:
        num1=list1.pop(0)
        num2=list2.pop(0)
        if num1>=num2:
            temp.append(num2)
            list1.insert(0,num1)
        else:
            temp.append(num1)
            list2.insert(0,num2)
    if len(list1) == 0:
        while(len(list2) != 0): temp.append(list2.pop(0))
    elif len(list2) == 0:
        while(len(list1) != 0): temp.append(list1.pop(0))
        
        
    return temp
    
if __name__=="__main__":
    list_ = [1]
    list2 = [-1,2,3,444,3,2,4,1,1,0]
    print(mergeSort(list2))
    
    