def compareTo(a, b):
    """
    Returns the same values as Java's compareTo()
    Usage:
        Java: a.compareTo(b)
        Python: compare(a, b)
    """
    
    len_a = len(a)
    len_b = len(b)
    
    if(a == b):
        return 0
    
    if(len_a > len_b or len_a == len_b):
        for i in range(0, len_b):
            if(ord(a[i]) != ord(b[i])):
                return ord(a[i]) - ord(b[i])
        return len_a-len_b

    else:
        for i in range(0, len_a):
            if(ord(a[i]) != ord(b[i])):
                return ord(a[i]) - ord(b[i])
        return len_a-len_b


def ignoreSpaces(a):
    """returns a string without spaces"""
    
    b = ""
    for i in a:
        if(i == ' '):
            continue
        else:
            b += i
    return b

def printArray(a):
    for i in a:
        print i
        
def printArray(a):
    for i in a:
        for j in i:
            print j,
        print ""
def printDict(a):
    for i in a:
        print i, ":", a[i]
