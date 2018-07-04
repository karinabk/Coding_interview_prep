```String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).```

#complexity O(n^3)
def compression(string):
    copy = string
    result = ""
    while len(string) != 0:
        i = 0
        while string[i] == string[i+1]:
            i += 1
            if i == len(string)-1:
                break
        result += string[i] + str(i+1)
        string = string.replace(string[i], "")

    if len(copy) > len(result):
        return result
    else:
        return copy
