import sys
import random
import math
from collections import Counter

# Read data
f = open(sys.argv[1], 'r')
X = []
l = f.readline()
while( l != ''):
	a = l.split()
	bu = []
	for i in range (0, len(a), 1):
		bu.append(float(a[i]))
	X.append(bu)
	l = f.readline()	
rows = len(X)
columns = len(X[0])
f.close()

# Read trainfile
f = open(sys.argv[2], 'r')
Original = {}
l = f.readline()
while( l != ''):
	a = l.split()
	Original[int(a[1])] = int(a[0])
	l = f.readline()
f.close()

def bootstrapagg(Original,X,rows,columns):
    nkey = list()
    sampleX =[]
    sampleOriginal = {}
    for i in Original.keys():
        nkey.append(i)   
    for i in range(0,len(nkey),1):
        rowselect = random.choice(nkey)
        sampleX.append(X[rowselect])
        sampleOriginal[i]= Original.get(rowselect)
    Xrows = len(sampleX)
    Xcolumns = len(sampleX[0])
    return (sampleX,sampleOriginal,Xrows,Xcolumns)

def ginicalc(X,Original,rows,columns,pridict_val,row_ori,col_ori,mOriginal,mX):
    ginivalues = []
    split = 0
    l3 = [0, 0]
    for j in range(0, columns, 1):
        ginivalues.append(l3)
    temp = 0
    col = 0    
    for j in range(0,columns,1):
        listcol = [item[j] for item in X]
        keys = sorted(range(len(listcol)), key=lambda k: listcol[k])
        listcol.sort()
        ginival = []
        prevgini = 0
        prevrow = 0
        for k in range(1, rows, 1):
            lsize = k
            rsize = rows - k
            lp = 0
            rp = 0
            for l in range(0, k, 1):
                if (Original.get(keys[l]) == 0):
                    lp += 1
            for r in range(k, rows, 1):
                if (Original.get(keys[r]) == 0):
                    rp += 1
            gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
            # print(gini)
            ginival.append(gini)
            prevgini = min(ginival)
            if (ginival[k - 1] == float(prevgini)):
                ginivalues[j][0] = ginival[k - 1]
                ginivalues[j][1] = k
        if (j == 0):
            temp = ginivalues[j][0]            
        if (ginivalues[j][0] <= temp):
            temp = ginivalues[j][0]
            col = j
            split = ginivalues[j][1]           
            if (split != 0):
                split = (listcol[split] + listcol[split - 1]) / 2    
    variable = 0
    m=0
    p=0
    for i in range(0, row_ori, 1):
        if(mOriginal.get(i) != None):
            if(mX[i][col] < split):
                if(mOriginal.get(i)== 0):
                    m += 1
                if(mOriginal.get(i) == 1):
                    p += 1
    if(m > p):
        left=0
        right=1
    else:
        left=1
        right=0
    for i in range(0,row_ori,1):
        if(mOriginal.get(i) == None):
            if(mX[i][col] < split):
                variable = left 
            else:
                variable = right
            if i in pridict_val:
                pridict_val[i].append(variable)
            else:
                pridict_val[i] = [variable]
    return (pridict_val)
pridict_val = dict()
row_ori=len(X)
col_ori=len(X)
mX=X
mOriginal=Original
for i in range (0,5,1):    
    sampleX,sampleOriginal,Xrows,Xcolumns = bootstrapagg(Original,X,rows,columns)    
    pridict_val = ginicalc(sampleX,sampleOriginal,Xrows,Xcolumns,pridict_val,row_ori,col_ori,mOriginal,mX)
    #print (len(pridict_val))

for k,v in pridict_val.items():
    count = Counter(pridict_val[k])
    a = count.most_common()[0]
    print(a[0],k)    