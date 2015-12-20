#! /usr/bin/python
# -*- encoding: utf-8 -*-
run = True
while run:
    while True:
        print 'ctrl + c to quit'
        word1 = raw_input('Vnesite prvo besedo: ')
        if (len(word1) != 0):
            if (word1 == 'x'):
                run = False
                break
            break

    while True:
        word2 = raw_input('Vnesite drugo besedo: ')
        if (len(word1) != 0):
            break

    word1_ord_count = 0
    word2_ord_count = 0

    for i, j in zip(word1, word2):
       word1_ord_count += ord(i)
       word2_ord_count += ord(j)

    print word1_ord_count
    print word2_ord_count
