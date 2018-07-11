```Given two (singly) linked lists, determine if the two lists intersect. Return the inter­
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting```   
   def intersection(llist1, llist2):
        tail1 = llist1.head
        tail2 = llist2.head
        inter = LinkedList()
        while True:
            tail1 = llist1.head
            tail2 = llist2.head
            while tail1.next != None:
                prev1 = tail1
                tail1 = tail1.next
            while tail2.next != None:
                prev2 = tail2
                tail2 = tail2.next
            if tail1.value==tail2.value:
                inter.add(tail1.value)
                prev1.next = None
                # prev2.next = None
            if prev1!=prev2:
                break
        if inter.head != None:
            return inter
        else:
            return False
            
            
  ```Implement a function to check if a linked list is a palindrome```          
    
    def palindrome(llist):
        run=llist.head
        temp = LinkedList()
        size = 0
        while run != None:
            run = run.next
            size += 1
        for i in range(int(size/2)):
            run = llist.head
            while run.next != None:
                prev=run
                run = run.next
            temp.add(run.value)
            prev.next=None
        run1 = llist.head
        run2 = temp.head
        while run1 != None and run2 != None:
            if run1.value != run2.value:
                return False
            run1=run1.next
            run2=run2.next
        return True
