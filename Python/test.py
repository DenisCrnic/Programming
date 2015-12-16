#! /usr/bin/python
#-*-encoding: utf-8-*-
from Person import *
from Family import *

def Main():
    denis = Person('Denis', 17, 165.5, 'male')
    undefined_persons = {'Denis' : denis}
    crnic = Family('Crnic', undefined_persons)
    print crnic

if __name__ == '__main__':
    Main()
