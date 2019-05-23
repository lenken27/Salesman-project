# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:23:54 2019

@author: Emre
"""

def get_path(n):
    start=np.where(city=='Ankara')
    l = list(range(n))
    l=np.delete(l,start)
    np.random.shuffle(l)
    l= np.insert(l,0,start)  
    return l

def draw_path(path):
    path = np.append(path,path[0])
    plt.plot(y[path],x[path],'-o')

def path_length(path):  #it is calculating from distancesmatrix
    path = np.append(path,path[0])
    dist=distances()
    def distance(i,j):
        return dist[i][j]
    total_length=0
    for i,j in zip(path[:-1],path[1:]):
        d=distance(i,j)
        total_length=total_length+d
    return total_length
    
l=get_path(n)
print('Any route length =',path_length(l))
draw_path(l)
plt.show()