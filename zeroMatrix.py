```Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
Complexity both O(n^2)
```

def zeroMatrix(matrix, num):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == num:
                row = i
                column = j
                break
    for i in range(len(matrix)):
        matrix[i][column] = 0
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
    return matrix


def stringRotation(s1, s2):
    count = 0
    wasHere = 0
    if len(s2) != len(s1):
        return False
    else:
        for i in range(len(s2)):
            j = 0
            while s2[i] == s1[j]:
                if i + 1 == len(s2):
                    wasHere = 1
                    start = j+1
                    break
                i += 1
                j += 1
            if i + 1 == len(s2) and wasHere == 0:
                return False
            elif wasHere==1:
                break
        for k in range(start + 1):
            if s1[start] != s2[k]:
                count += 1
            start+=1
        if count == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(zeroMatrix(matrix, 5))

    s1="ohell"
    s2="hello"
    print(stringRotation(s1,s2))
