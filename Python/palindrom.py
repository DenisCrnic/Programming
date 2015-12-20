#! /usr/bin/python
#-*-coding: utf-8-*-

from functions import ignoreSpaces

run = True
while run:
    while True:
        a = raw_input('Input (q - to quit): ')
        if (a == 'q'):
            run = False
            break
        if (len(a) == 0):
            print '(EMPTY INPUT) u must enter something!'
            continue
        else:
            a = ignoreSpaces(a)
            b = a.decode('utf8')[::-1].encode('utf8')
        if (a.lower() == b.lower()):
            print 'IS palindrome'
        else:
            print 'IS NOT palindrome'

print 'BYE!'
