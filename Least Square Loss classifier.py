import sys, math, random

#Read DataFile

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


#Read TrainFile

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

#Generate random weights

w = []
for i in range(0, columns, 1):
	w.append(0)
	w[i] = random.uniform(-0.01, 0.01)

prev_error = 0
count = 0
while(1):
	count +=1
 #Original minus W.X

	dot_prod = []
	d = []
	for i in range(0, len(Original), 1):
		dot_prod.append(0)
		d.append(0)
		for j in range(0, columns, 1):
			dot_prod[i] = dot_prod[i] + (X[i][j]*w[j])
		d[i] = Original[i] - dot_prod[i]

 #Find error

	error = 0
	for i in range(0, len(Original), 1):
		error +=  ((d[i])**2)/2
	
 #Compare error

	if (prev_error != 0):
		if (prev_error - error <= 0.001):
			break
	
 #Compute difference in weights
	Eta = 0.001
	del_E = []
	for i in range(0, columns, 1):
		del_E.append(0)
		for j in range(0, len(Original), 1):
			del_E[i] = del_E[i] + (d[j]*X[j][i])
			
	del_w = []
	for i in range(0, columns, 1):
		del_w.append(0)
		del_w[i] = Eta * del_E[i]
		
 #Change in weights

	for i in range(0, columns, 1):
		w[i] = w[i] + del_w[i]
		
 #Change Errors
	prev_error = error

#Hyperplane and distance from origin
new_w = 0
for i in range(0, columns-1, 1):
	new_w = new_w + w[i+1]**2

new_w = math.sqrt(new_w)
distance = abs(w[0]/new_w)
print("Distance from Origin to plane is %s" %distance)

#Prediction for rest of DataFile

for i in range(0, rows, 1):
	if (Original.get(i) == None):
		out = 0
		for j in range(0, columns, 1):
			out = out + (X[i][j]*w[j])
		if (out > 0):
			print('1', i)
		else:
			print('0', i)