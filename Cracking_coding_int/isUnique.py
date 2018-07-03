# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?



# Complexity O(n)
def isUnique(str):
    list_ = list(str)
    set_ = set(list_)
    if len(set_) < len(list_):
        return False
    else:
        return True


# Complexity O(n^2)
def isUnique(string):
    for i in range(len(string)):
        char = string[0]
        string = string[1:len(string)]
        if char in string: return False
    return True
    
