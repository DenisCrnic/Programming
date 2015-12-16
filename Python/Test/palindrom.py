#-*-coding: utf-8-*-

from numpy.core.defchararray import lower


def ignoreSpaces(a):
    """Returns a string without spaces"""
    b = ""
    for i in a:
        if(i == ' '):
            continue
        else:
            b += i
    return b

run = True
while(run):
    while(True):
        a = (raw_input("Input (q - to quit): "))
        if(a == "q"):
            run = False
            break
        if(len(a) == 0):
            print "(EMPTY INPUT) u must enter something!"
            continue
        else:
            a = ignoreSpaces(a)
            b = a.decode('utf8')[::-1].encode('utf8')
    
        if(lower(a) == lower(b)):
            print "IS palindrome"
        else:
            print "IS NOT palindrome"
            
print "BYE!"