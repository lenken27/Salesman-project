# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:24:54 2019

@author: Emre
"""

def minumun_distance(dist):
    total=0
    a=5
    b=0
    min_distance=0
    for i in range (80):
        a=5
        k=0
        a=b
        for j in range(80):   
            if dist[k][a]<=dist[j+1][a] and dist[k][a]!=0:
                min_distance=(dist[k][a])
                b=k
            else:
                k=j+1
                
        dist[:][a]=0
        total=total+min_distance    

    return total

def draw_path(path):
    path = np.append(path,path[0])
    plt.plot(y[path],x[path],'-o')