#-*- encoding: utf-8 -*-

import webbrowser
from time import sleep
from selenium import webdriver

dr = webdriver.Chrome()

run = True
while run:
    url = "http://" + raw_input("Input url: http://")
    
    while True:
        try:
            times = input("How many times do you want to open this tab: ")
            sleep_time = input("open tab each x seconds x: ")
            break
        except:
            "Input number!"
    for i in range(times):
        sleep(sleep_time)
        webbrowser.open(url)
        dr.close