# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:23:26 2019

@author: Emre
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd


def coordinates():   
    loc = ('Coordinates.xlsx')
    wb = xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    city=[]
    x=[]
    y=[]
    for i in range(81): 
        a = sheet.cell_value(i+1,1)
        city = np.append(city,a)        
        b = sheet.cell_value(i+1,2)
        x = np.append(x,b)        
        c = sheet.cell_value(i+1,3)
        y = np.append(y,c)
    
    return city,x,y

def distances():
    loc = ('distancematrix.xls')
    wb = xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    dist=[]
    x=np.arange(0,81*81,81)
    
    for i in range(81):
        for j in range(81):
            a = sheet.cell_value(i+3,j+2)
            dist.append(a)  
            
    for i in range(81):
        dist[x[i]+i]=0
    dist=np.reshape(dist,(81,81))
    
    return dist

city,x,y=coordinates()

dist=distances()