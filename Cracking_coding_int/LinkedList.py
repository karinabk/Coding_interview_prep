class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size=0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size+=1

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                self.size-=1
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
        self.size-=1

    def printList(self):
        temp = self.head
        while (temp):
            print(" {0}".format(temp.data))
            temp = temp.next
```Remove Dups! Write code to remove duplicates from an unsorted linked list.```
    def removeDups(self):
        vals=[]
        runner=self.head
        while runner!=None:
            if runner.data in vals:
                self.deleteNode(runner.data)
            else:
                vals.append(runner.data)
            runner=runner.next
```Implement an algorithm to find the kth to last element of a singly linked list```
    def kthToLast(self,index):
        runner=self.head
        for i in range(index):
            runner=runner.next
        while runner!=None:
            print(" {0}".format(runner.data))
            runner=runner.next
```Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node```
    def deleteMiddle(self):
        runner=self.head
        for i in range(int(self.size/2)):
            runner=runner.next
        self.deleteNode(runner.data)
```Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.```
    def partition(self,num):
        runner = self.head
        new_ll=LinkedList()
        while runner!=None:
            temp=runner.data
            if temp<num:
                new_ll.push(runner.data)
            runner=runner.next
        runner = self.head
        while runner!=None:
            temp=runner.data
            if temp>=num:
                new_ll.push(runner.data)
            runner=runner.next
        return new_ll

