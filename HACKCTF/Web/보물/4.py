# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:06:23 2020

@author: msi
"""

import requests
from selenium import webdriver
driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
url = "http://ctf.j0n9hyun.xyz:2025/?page="

i = 1;
while(1):
    response = requests.get(url+str(i))
    if "HackCTF" in response.text:
        driver.get(url+str(i))
        print(i)
        break;
    print(f"/page={i}에 flag없음")
    i+=1