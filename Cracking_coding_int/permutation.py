#Check Permutation: Given two strings, write a method to decide if one is a permutation of the
#other

# complexity O(n^2)
def permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    list2 = list(string2)
    for i in string1:
        for j in list2:
            if j == i:
                list2.remove(j)
                break
    if len(list2) == 0:
        return True
    else:
        return False

#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string.

# complexity O(n)
def URLify(string):
    string = string.strip()
    list_=list(string)
    for i in range(len(list_)):
        if list_[i]==' ':
            list_[i]='%20'
    return ''.join(list_)
