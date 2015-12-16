#-*- coding: utf-8 -*-
import sys
from Crypto.Random.random import randrange
def enkripcija(a, key):
    x = ""
    for i in a:
        y = str(ord(i) + key)
        if(len(y) == 1):
            x = x + "00" + y
        elif(len(y) == 2):
            x = x + "0" + y
        else:
            x += y
    return x
    
def dekripcija(a, key):
    x = ""
    for i in range(0, len(a), 3):
        x +=chr(int(a[i:i+3])-key)
    return x

while True:
    select = raw_input("""\
e - enkripcija besedila
d - dekripcija besedila
q - quit
select: """)
    if(select == "e"):
        a = raw_input("Vnesite besedilo: ")
        b = randrange(100,700)
        print "key:", b
        print enkripcija(a, b), "\n\n"
    elif(select == "d"):
        a = raw_input("Vnesite besedilo: ")
        while True:
            try:
                b = input("Vnesite kljuc: ")
                break
            except:
                print "vnos mora biti stevilo"
        print dekripcija(a, b), "\n\n"
    elif(select == "q"):
        break
    else:
        print "neveljavna selekcija"