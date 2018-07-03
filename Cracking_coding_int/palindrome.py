#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
#drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
#is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    # complexity O(n^2)
 def palindromePermutation(string):
        string = string.replace(" ", "").lower()
        print(string)
        counterOdd = 0
        for i in string:
            if string.count(i) % 2 != 0:
                counterOdd += 1
        if counterOdd > 1:
            return False
        else:
            return True
            
#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees
       #complexity O(n^2)
 def rotate90(matrix):
    N = len(matrix)
    result = [[0 for x in range(N)] for y in range(N)]
    for i in range(len(matrix)):
        j = 0
        k = len(matrix) - 1
        while j < len(matrix):
            result[k][i] = matrix[i][j]
            k -= 1
            j += 1
    return result
    
 if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 0],
              [5, 6, 7, 8, 0],
              [9, 10, 11, 12, 0],
              [13, 14, 15, 16, 0],
              [17, 18, 19, 20, 0]]
    matrix2 = [[1, 2], [3, 4]]
    # print(rotate90(matrix))
