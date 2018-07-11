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
```Suppose the digits are stored in forward order. Repeat the above problem.``

   def sum2(llist1, llist2):
        result = LinkedList()
        count = 0
        while True:
            prev1 = runner1 = llist1.head
            prev2 = runner2 = llist2.head
            if runner1!=None:
                while runner1.next != None:
                    prev1 = runner1
                    runner1 = runner1.next
            if runner2!=None:
                while runner2.next != None:
                    prev2 = runner2
                    runner2 = runner2.next
            if runner1 == None:
                num1 = 0
            else:
                num1 = runner1.value
            if runner2 == None:
                num2 = 0
            else:
                num2 = runner2.value
            input = num1 + num2 + count
            if input >= 10:
                input = input - 10
                count = 1
            else:
                count = 0
            if result.head == None:
                result.add(input)
            else:
                result.head = LinkedListNode(input, result.head)
            if prev1 == runner1 and prev2 != runner2:
                llist1.head = None
                prev2.next = None
            if prev1 != runner1 and prev2 == runner2:
                llist2.head = None
                prev1.next = None

            if runner1 == prev1 and runner2 == prev2:
                break
        if count == 1:
            result.head = LinkedListNode(1, result.head)
        return result
