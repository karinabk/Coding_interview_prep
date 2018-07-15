```Q1. Given an array of integers, you need to find the local maxima.
Example : [1 3 5 4 7 10 6]

Output : 5 or 10

Explanation : Any of the local maxima can be the output. 
Here 5 is greater than 3 and 4, 10 is greater than 7 and 6. ```

def localMax(list_):
    localMax = []
    if len(set(list_)):
        return list_[0]
    for i in range(1, len(list_) - 1):
        if list_[i] > list_[i + 1] and list_[i] > list_[i - 1]:
            localMax.append(list_[i])
    return localMax


def findHelper(arr, low, high, n):
    mid = int(low + (high - low) / 2)
    if ((arr[mid] >= arr[mid + 1] or mid == n - 1) and
            (arr[mid] >= arr[mid - 1] or mid == 0)):
        return arr[mid]

    elif mid > 0 and arr[mid] < arr[mid - 1]:
        return findHelper(arr, low, (mid - 1), n)
    else:
        return findHelper(arr, (mid + 1), high, n)


def findPeak(arr, n):
    return findHelper(arr, 0, n - 1, n)

```Q2. Given a sequence of brackets, how will you identify if its valid or not.

Example : ({[][]})

Output : Valid

Explanation : Every opening bracket has a closing bracket.

Example : ({[]]}) 

Output : Invalid 

Explanation : Every opening bracket does not have a closing bracket.
```
def brackets(string1):
    input = list(string1)
    brackets={'[':']',']':'[','(':')',')':'(','{':'}','}':'{'}
    temp=[]
    if len(input)%2!=0:
        return False
    if input[0]==']' or input[0]==')' or input[0]=='}':
        return False
    key1=input.pop()
    temp.append(key1)
    while(len(input)!=0):
        key2 = input.pop()
        if brackets[key1]!= key2:
            temp.append(key1)
            temp.append(key2)
        key1=temp.pop()
    if len(temp)==0:
        return True
    else:
        return False




if __name__ == "__main__":
        arr = [1, 3, 5, 4, 3, 7, 10, 6]
        # num = findPeak(arr,len(arr))
        str="({[]]})"
        print(brackets(str))
