#! /usr/bin/python
# -*- encoding: utf-8 -*-

def printDict(n):
    if len(n) == 0:
        return
    else:
        print n
        return n[-1]
def main():
    lista = ['Denis', 'mama', 'tata']
    print printDict(lista)

if (__name__ == '__main__'): main()
