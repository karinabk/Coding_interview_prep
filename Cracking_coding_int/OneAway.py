```There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away```

#complexity O(N)

def oneAway(origin, modified):
    list1 = list(origin)
    list2 = list(modified)
    count = 0
    i = 0
    if len(origin) + 1 == len(modified) or len(origin) == len(modified) + 1:
        while i != len(list1) and i!=len(list2):
            if list1[i] != list2[i] and count > 0:
                return False
            if list1[i] != list2[i] and count == 0:
                count += 1
                if len(origin) > len(modified):
                    list1.remove(list1[i])
                else:
                    list2.remove(list2[i])
            i+=1
        return True
    elif len(origin) == len(modified):
        while i != len(list1):
                if list1[i] != list2[i]:
                    count += 1
                i+=1
        if count <= 1:
            return True
        else: return False
    else:
        return False
