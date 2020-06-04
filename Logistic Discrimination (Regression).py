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
	Original[int(a[1])] = int(a[0])
	l = f.readline()
f.close()

# Generate random weights
w = []
for i in range(0, columns, 1):
	w.append(random.uniform(-0.01, 0.01))
	
#dot product function
def dot_product(arg1,arg2):
        dp1=0
        for j in range(0,columns,1):
            dp1 += arg1[j]*arg2[j]
        return dp1;	

#gradient descent iteration
eta=0.01
theta=0.0000001
prev_obj=0.0
'''
for i in range(0,rows,1):
	if(Original.get(i)!= None):
		dp=-1*dot_product(w,X[i])
		exponential = math.exp(-1*dp)
		if (Original.get(i) == 1):
			prev_obj-= math.log(1/(1+exponential))     #math.log(1+exponential) 
		elif (Original.get(i) == 0):
			prev_obj-= math.log(exponential/(1+exponential))    #math.log((1+exponential)/exponential)      #
'''
while (1):
	gradient=[]
	for j in range(0,columns,1):
		gradient.append(0)

	for i in range (0,rows,1):
		if (Original.get(i) != None):
			dp=dot_product(w,X[i])
			exponential = math.exp(dp)
			for j in range (0,columns,1):
				if(Original[i]==1):
					gradient[j]+=float(X[i][j])*(1-(1/(1+exponential)))
				elif(Original[i]==0):
					gradient[j]+=float(X[i][j])*(-1/(1+exponential))
		    
        #update w
	for j in range (0,columns,1):
		w[j]=w[j]-eta*gradient[j]
	error=0.0
	for i in range(0,rows,1):  
		if(Original.get(i)!= None):
			dp=dot_product(w,X[i])
			exponential = math.exp(dp)
			if (Original.get(i) == 1):
				error-= math.log(1/(1+exponential))     #math.log(1+exponential)
			elif (Original.get(i) == 0):
				error-= math.log(exponential/(1+exponential))    #math.log((1+exponential)/exponential)
	if (abs(prev_obj-error)<=theta):  
		break
	prev_obj=error
	print (error)
for i in range(1, columns, 1):
	print(-1*w[i])
	
#Distance
distance = 0.0 
for i in range(1, columns, 1):
	distance += w[i]**2
print(math.sqrt(distance))
distance = w[0]/(math.sqrt(distance))	
print(-1*distance)
#prediction
for i in range(0,rows,1):
    if (Original.get(i) == None):
        dp=0
        for j in range(0,columns,1):
            dp+=X[i][j]*w[j]
            
        if dp>0:
            print("0,",i)
        else:
            print("1,",i)