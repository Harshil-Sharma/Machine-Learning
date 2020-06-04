import sys
import math
import random 
from collections import defaultdict
import csv

def distance(data, length):
    sum1 = sum([(m - n)**2 for m, n in zip(data, length)])
    return math.sqrt(sum1)
def find_cluster(data, length):
    d = defaultdict(list)
    cen = []
    for i in range(0,len(data)):
        temp = []
        for j in range(0,len(length)):
            temp.append(distance(data[i], length[j]))
        indx = temp.index(min(temp))
        d[indx].append(data[i])
    for key in d:
        temp = d[key]
        cen.append([sum(l)/len(l) for l in zip(*temp)])
    return cen
def has_converged(prev, new):
    return (set([tuple(a) for a in prev]) == set([tuple(a) for a in new]))
def k_means(data, length):
    c1 = random.sample(data, length)
    while True:
        c1_new = find_cluster(data, c1)
        if has_converged(c1, c1_new):
            c1  = c1_new
            break
        c1  = c1_new
    for i in range(0,len(data)):
        temp = []
        for j in range(0,len(c1)):
            temp.append(distance(data[i], c1[j]))
        indx = temp.index(min(temp))
        print(indx, i)
    return c1
if __name__ == '__main__': 
    datafile = sys.argv[1]
    f=open(datafile)    
    data=[]
    l=f.readline()
    while (l != ''):
        a=l.split()
        l2=[]
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        data.append(l2) 
        l=f.readline()
    length=sys.argv[2]
    mu = k_means(data, int(length))