#-*-coding: utf-8-*-
from encodings.idna import ToASCII

def compare(a, b):
    if(a == b):
        return 0
    if(len(a) > len(b) or len(a) == len(b)):
        for i in range(0, len(b)):
            if(ord(a[i]) != ord(b[i])):
                return ord(a[i]) - ord(b[i])
        return len(a)-len(b)

    else:
        for i in range(0, len(a)):
            if(ord(a[i]) != ord(b[i])):
                return ord(a[i]) - ord(b[i])
        return len(a)-len(b)
            
            
a = raw_input("A: ")
b = raw_input("B: ")

print compare(a, b)