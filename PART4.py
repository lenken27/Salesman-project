# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:25:50 2019

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

def get_path(n):
    start=np.where(city=='Ankara')
    l = list(range(n))
    l=np.delete(l,start)
    np.random.shuffle(l)
    l= np.insert(l,0,start)  
    return l

#def get_path_length(path): #it is calculating from coordinates
#    path = np.append(path,path[0])
#    total_length = 0.0
#    for i in range(len(path)-1):
#        j = path[i]
#        k = path[i+1]
#        dist = np.sqrt((x[j]-x[k])**2+(y[j]-y[k])**2)
##        print('%d %d %d %5.2f %5.2f %5.2f'%(i,j,k, x[i],y[i], dist))
#        total_length = total_length+dist  
#    return total_length

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

def draw_path(path):
    path = np.append(path,path[0])
    plt.plot(y[path],x[path],'-o')
  
def cross_over(gene1,gene2, mutation=0.5):
    
  r = np.random.randint(len(gene1)) # cross over location
  newgene = np.append(gene1[:r],gene2[r:]) # may be a defunct gene
    
  missing = set(gene1)-set(newgene)
  elements, count = np.unique(newgene, return_counts=True)
  duplicates = elements[count==2]
  duplicate_indices=(newgene[:, None] == duplicates).argmax(axis=0)
  
  newgene[duplicate_indices]=list(missing) # now proper.
  
  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,len(newgene),2)
    newgene[[i1,i2]] = newgene[[i2,i1]] 
  return newgene

def create_initial_population(m,n):
    population = []
    fitness = []
    for i in range(m):
        gene = get_path(n)
        path_length1 = path_length(gene)
        
        population.append(gene)
        fitness.append(path_length1)
  
    population = np.array(population)
    fitness = np.array(fitness)  
    sortedindex = np.argsort(fitness)
    return population[sortedindex], fitness[sortedindex]

def next_generation(population):
    pop = []
    fit = []
    i=0
    f=int(np.sqrt(len(population)))
    for gene1 in population[:f]:
        for gene2 in population[:f]:
            i=i+1      
            x =  cross_over(gene1,gene2)
            l = path_length(x)
            pop.append(x)
            fit.append(l)
  
    population = np.array(pop)
    fitness = np.array(fit)  
    sortedindex = np.argsort(fitness)
    return population[sortedindex], fitness[sortedindex]


city,x,y=coordinates()

dist=distances()
fig, ax =plt.subplots(figsize=((45-26),(42-36)))
plt.plot(y,x,'o')
plt.show()
n=len(x)
n_population=100


l=get_path(n)



population, fitness  = create_initial_population(n_population,n)

for i in range(500):
  print(i)
  population, fitness=next_generation(population)
  print('Fitness length =',fitness.min(),'\nFitness average length =',fitness.mean())

  best_path = population[0]
  draw_path(best_path)
  plt.show()
  
  plt.plot(fitness)
  plt.show()