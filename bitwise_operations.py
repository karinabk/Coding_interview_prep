#Exercise: count the number of bits that are different between two numbers

def diff1(x,y):
    mask = x^y
    count =0
    while(mask!=0):
        count+=1&mask
        mask=mask>>1
    return count


def diff(x,y):
    mask = bin(x^y)
    count =0
    for i in mask:
        if i=='1':
            count+=1
    print(mask)
    return count

if __name__=="__main__":
    print(diff1(3,222))
    
