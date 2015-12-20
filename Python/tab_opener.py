#! /usr/bin/python
#-*- encoding: utf-8 -*-

import webbrowser
from time import sleep

run = True
while run:
    url = 'http://' + raw_input('Input url: http://')
    while True:
        try:
            times = input('How many times do you want to open this tab: ')
            if (times > 1):
                sleep_time = input('open tab each x seconds x: ')
            break
        except:
            'Input number!'
    for i in range(times):
        if (times > 1):
            sleep(sleep_time)
        webbrowser.open(url)
