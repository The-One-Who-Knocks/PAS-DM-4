import os
import sys
import numpy as np
import math
import random
import matplotlib.pylab as plt

L=70
N=L**2
T=1
beta=1/T
p=1-math.exp(-2*beta)

def magnetization(conf):#sum of the spins
    m=0
    siz=(np.size(conf,1))-1
    for i in range(siz+1):
        for j in range(siz+1):
            m=m+conf[i][j]
    return m

def magnetization_delta(cluster):#computes the magnetization variation of the system when flipping the cluster
    k=cluster[0]    
    return conf[k[0],k[1]]*np.size(cluster)

def energy(conf):#eenrgy of the system for a given configuration
    e=0
    siz=(np.size(conf,1))-1
    for i in range(siz+1):
        for j in range(siz+1):
            if i==siz and not j==siz: 
                e=e-conf[i][j]*conf[i][j+1]
            elif j==siz and not i==siz:
                e=e-conf[i][j]*conf[i+1][j]
            elif not i==siz and not j==siz:
                e=e-conf[i][j]*conf[i+1][j]-conf[i][j]*conf[i][j+1]
    return e
    
def ini_conf(L):#generates a configuration
    conf=np.zeros((L, L))
    for i in range(L):
        for j in range(L):
            if (random.random()<0.5): 
                conf[i][j]=1
            else: 
                conf[i][j]=-1
    return conf

def neighbours(conf,seed_site):#returns the neighbours of a seed_spin if they are identical to the seed_spin
    k=[]
    if  (0 <= seed_site[0]+1 < L) and conf[seed_site[0],seed_site[1]]==conf[seed_site[0]+1,seed_site[1]]:
        k.append([seed_site[0]+1,seed_site[1]])
    if  (0 <= seed_site[0]-1 < L) and conf[seed_site[0],seed_site[1]]==conf[seed_site[0]-1,seed_site[1]]:
        k.append([seed_site[0]-1,seed_site[1]])
    if  (0 <= seed_site[1]+1 < L) and conf[seed_site[0],seed_site[1]]==conf[seed_site[0],seed_site[1]+1]:
        k.append([seed_site[0],seed_site[1]+1])
    if  (0 <= seed_site[1]-1 < L) and conf[seed_site[0],seed_site[1]]==conf[seed_site[0],seed_site[1]-1]:
        k.append([seed_site[0],seed_site[1]-1])
    return k
                
def cluster_construction(conf,seed_site):#returns the cluster 
    Cluster=[]
    Cluster.append(seed_site)
    F_old=[]
    F_old.append(seed_site)
    while not (F_old==[]):
        F_new=[]
        for i in F_old:
            for j in neighbours(conf,i):
                if not j in Cluster:
                    if random.random()<p:
                       F_new.append(j)
                       Cluster.append(j)
        F_old=F_new
    return Cluster

def energy_delta(conf,cluster):#computes the energy variation of the system when flipping the cluster
    e=0    
    for k in cluster:
        if (0 <= k[0]+1 < L) and ([k[0]+1,k[1]] not in cluster): 
            e=e+conf[k[0]+1,k[1]]*conf[k[0],k[1]]*2
        if (0 <= k[0]-1 < L) and ([k[0]-1,k[1]] not in cluster):  
            e=e+conf[k[0]-1,k[1]]*conf[k[0],k[1]]*2
        if (0 <= k[1]+1 < L) and ([k[0],k[1]+1] not in cluster): 
            e=e+conf[k[0],k[1]+1]*conf[k[0],k[1]]*2        
        if (0 <= k[1]-1 < L) and ([k[0],k[1]-1] not in cluster): 
            e=e+conf[k[0],k[1]-1]*conf[k[0],k[1]]*2
    return e

#int main()
conf=ini_conf(L)
plt.figure(1)
plt.imshow(conf, cmap = 'Blues', interpolation='nearest')
t=0
i=0
times=[]
energies=[]
energie=energy(conf)
m=magnetization(conf)
ms=[]
while t<30:
    times.append(t)
    energies.append(energie)
    ms.append(m)    
    seed_site=[random.randint(0,L-1),random.randint(0,L-1)]#select a random spin
    cluster=cluster_construction(conf,seed_site)#construct a cluster arround this spin
    delt=energy_delta(conf,cluster)#compute the energy variation of the flip
    energie=energie+delt
    m=m+magnetization_delta(cluster)#compute the magnetization variation of the flip    
    for l in cluster:#Do the flip
        conf[l[0],l[1]]=-conf[l[0],l[1]]
    t=t+np.size(cluster)/N#increase time    
    i=i+1    
    print(t)
    #plt.figure(2)
    #plt.imshow(conf, cmap = 'Blues', interpolation='nearest')#show the system. Takes a lot of time.
    #plt.pause(0.000001) 

for i in range(np.size(ms)):
    ms[i]=np.abs(ms[i])/N
for i in range(np.size(energies)):
    energies[i]=(energies[i])/N
plt.figure(3)
plt.plot(times,energies)
plt.xlabel('t')
plt.ylabel('energy per spin')
plt.figure(4)
plt.plot(times,ms)
plt.xlabel('t')
plt.ylabel('magnetization per spin')
plt.show()
