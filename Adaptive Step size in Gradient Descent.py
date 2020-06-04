import math, sys, random

# Read data
f = open(sys.argv[1], 'r')
X = []
l = f.readline()

while( l != ''):
	a = l.split()
	bu = [1]
	for i in range (1, len(a)+1, 1):
		bu.append(float(a[i-1]))
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
	if (int(a[0]) == 0):
		a[0] = -1
	Original[int(a[1])] = int(a[0])
	l = f.readline()
f.close()

#dot product function
def dot_product(arg1,arg2):
        dp1=0
        for j in range(0,columns,1):
            dp1 += arg1[j]*arg2[j]
        return dp1;

#Initialize w
w=[]
for j in range(0,columns,1):
    w.append(0)
for j in range(0,columns,1):
	w[j]=0.02*random.uniform(0,1)- 0.01	

#gradient descent iteration
eta=0.001
theta=0.001
prev_obj=0.0
for i in range(0,rows,1):
    if(Original.get(i)!= None):
        dp=dot_product(w,X[i])
        prev_obj+=max(0,1-Original[i]*dp)
#print("prev",prev_obj)
count=0
eta_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001,0.0000001,0.00000001,0.000000001, 0.0000000001, 0.00000000001 ]
while True:
    gradient=[]
    for j in range(0,columns,1):
        gradient.append(0)
    
    for i in range (0,rows,1):
        if (Original.get(i) != None):
            dp=dot_product(w,X[i])
            for j in range (0,columns,1):
                if(dp*Original[i]<1):
                    gradient[j]+=-1*float(X[i][j])*Original[i]
                else:
                    gradient[j]+=0
		    #gradient.append(float((Original[i]-dp)*X[i][j]))
    bestobj = 1000000000000
    obj=0.0
    #count=0
    for k in range(0, len(eta_list),1):
        eta=eta_list[k]
        #count+=1
        for j in range(0,columns,1):
            w[j]=w[j]-eta*gradient[j]
        #print("w2",w)
        error1=0.0
        for i in range(0,rows,1):
            if(Original.get(i)!= None):
                dp=dot_product(w,X[i])
                error1+=max(0,1-Original[i]*dp)
        obj=error1
        if(obj<bestobj):
            bestobj=obj
            besteta=eta
        for j in range(0,columns,1):
            w[j]=w[j]+eta*gradient[j]
        #print("w3",w)
        
        #update w
    eta=besteta
    for j in range (0,columns,1):
        w[j]=w[j]-eta*gradient[j]
    error=0.0
    for i in range(0,rows,1):  
        if(Original.get(i)!= None):
            dp=dot_product(w,X[i])
            error+=max(0,1-Original[i]*dp)
    #print(abs(prev_obj-error))
    if abs(prev_obj-error)<=theta:  
        break
    #print(abs(prev_obj-error))
    prev_obj=error
    count+=1
#distance from origin calculation
#print(count)
#print("w vector: ")
normw=0
for j in range(0,columns-1,1):
	#print(abs(w[j]),)
	normw += w[j]**2

normw = math.sqrt(normw)
d_origin = abs(w[len(w)-1]/normw)
#print("distance from origin: ",d_origin)

#prediction
for i in range(0,rows,1):
    if (Original.get(i) == None):
        dp=0
        for j in range(0,columns,1):
            dp+=X[i][j]*w[j]
            
        if dp>0:
            print("1",i)
        else:
            print("0",i)