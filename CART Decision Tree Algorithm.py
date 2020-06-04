import math, sys, random

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
l1 = [0, 0]
gini_value=[]
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
 
for i in range(0, columns, 1):  
    gini_col = []
    gini=0.0
    cu_col=[]
    for k in range(0, rows, 1):
        cu_col.append(l1)
    cur_col=[]
    for k in range(0,rows,1):
        cu_col[k][0]=X[k][i]
        cu_col[k][1]=Original.get(k) 
        d=[cu_col[k][0],cu_col[k][1]]
        cur_col.append(d)
    cur_col = sorted(cur_col,key=lambda l:l[0])
    #print(cur_col)
    k=0
    for k in range(1, rows,1):
        lsize = k
        rsize = rows - k
        lp = 0
        rp = 0
        for col_v in range(0,k,1):
            if(cur_col[col_v][1] == 0):
                lp+=1
        for col_v in range(k,rows,1):
            if(cur_col[col_v][1] == 0):
                rp+=1
        gini = (lsize / rows) * (lp / lsize) * (1 -(lp / lsize)) + (rsize / rows) * (rp / rsize) * (1- (rp / rsize))
        val=[gini,cur_col[k][0],i]
        gini_col.append(val)        
    gini_col_sort=sorted(gini_col,key=lambda l:l[0])
    gini_value.append(gini_col_sort[0])
final_opt = sorted(gini_value,key=lambda l:l[0])
print( " Split",final_opt[0][1],"\n","Column",final_opt[0][2],"\n","Gini",final_opt[0][0])