# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:19:33 2020

@author: user
"""


c = 'hreCp1_ev_s117nr_ys17eer132n_5'
key = '465132'
start=0
end=6
while(end<35):
    b = c[start:end]
    for i in key:
        i = int(i)-1
        print(b[i],end = '')
    start+=6
    end+=6
        
        
    