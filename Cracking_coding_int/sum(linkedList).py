   ```You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list```
   def sum(llist1, llist2):
        runner1 = llist1.head
        runner2 = llist2.head
        result = LinkedList()
        count = 0
        while runner1 != None or runner2 != None:
            if count == 1:
                input = 1
                count = 0
            else:
                input = 0
            if runner2==None:
                temp2=0
            else:
                temp2=runner2.data
            if runner1==None:
                temp1=0
            else:
                temp1 = runner1.data
            if temp1 + temp2+input >= 10:
                result.push(temp1 + temp2 - 10 + input)
                count = 1
            else:
                result.push(temp1 + temp2 + input)
            if runner1!=None:
                runner1 = runner1.next
            if runner2!=None:
                runner2 = runner2.next
        if count==1:
            result.push(1)
        return result
```Suppose the digits are stored in forward order. Repeat the above problem.```
```Does not work yet    ```

    def sum2(llist1, llist2):

        result = LinkedList()
        count = 0
        i = 0
        while True:
            runner1 = llist1.head
            runner2 = llist2.head
            while runner1.next!=None and runner2.next!=None:
                runner1 = runner1.next
                runner2 = runner2.next
            if count == 1:
                input = 1
                count = 0
            else:
                input = 0
            if runner1.data + runner2.data >= 9:
                result.push(runner1.data + runner2.data - 10 + input)
                count = 1
            else:
                result.push(runner1.data + runner2.data + input)
            i += 1
            if runner1 == llist1.head or runner2 == llist2.head:
                break
            runner1=None
            runner2=None
        return result
