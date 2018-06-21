#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:47:31 2018

@author: karina
"""

class maxHeap:
    def __init__(self):
        self.myList=[]
        
    def insert(self, num):
        self.myList.append(num)
        self.__sift_up()
        print(self.myList)
        
    def get_size(self):
        return len(self.myList)
    
    def is_empty(self):
        if len(self.myList==0):
            return True
        else:
            return False
        
    def extract_max(self):
        self.__swap(0,len(self.myList)-1)
        maxV = self.myList.pop(len(self.myList)-1)
        self.sift_down()
        print(maxV)
        
    def remove(self,ind):
        self.myList.pop(ind)
        
    def heapify(self, newList):
        for i in newList:
            self.insert(i)
        return self.myList
        
    
        
    def sift_down(self):
        index = 0
        childLeftIndex=1
        childRightIndex=2
        while childLeftIndex<=len(self.myList)-1:
            
            biggerNum=childLeftIndex
            if childRightIndex<=len(self.myList)-1 \
                and self.myList[childRightIndex]>self.myList[childLeftIndex]:
                    biggerNum=childRightIndex
            if self.myList[index]>=self.myList[biggerNum]:
                break
            else:
                self.__swap(index,biggerNum)
            index=biggerNum
            childLeftIndex=index*2+1
            childRightIndex=index*2+2
            
                    
        
        
    def __swap(self,index1,index2):
        temp = self.myList[index1]
        self.myList[index1]=self.myList[index2]
        self.myList[index2]=temp
        
        
    def __sift_up(self):
        index = len(self.myList)-1
        parentIndex=int((index-1)/2)
        while parentIndex>=0 and self.myList[index]>self.myList[parentIndex]:
            
            self.__swap(index,parentIndex)
            index=parentIndex
            parentIndex=int((index-1)/2)
    
    def get_max(self):
        return self.myList[0]
    
    def toString(self):
        print(self.myList)
    
if __name__=="__main__":
    newHeap=maxHeap()
#    newHeap.insert(2)
#    newHeap.insert(1)
#    newHeap.insert(3)
#    newHeap.insert(170)
#    newHeap.insert(3)
#    newHeap.insert(18)
#    newHeap.insert(999)
#    newHeap.extract_max()
#    newHeap.toString()
#    newHeap.extract_max()
#    newHeap.toString()
#    newHeap.insert(9)
#    newHeap.toString()
    
    list2=[9,87,6,5,43,54,67,8]
    
    print(newHeap.heapify(list2))
    
    
        
        
    
        