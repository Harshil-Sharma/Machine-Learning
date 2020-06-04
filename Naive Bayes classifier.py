import sys
import math

 #Read data file 

  
f = open(sys.argv[2], 'r')                                       
data = []
l = f.readline()

while(l != ''):
	a = l.split()
	l1 = []
	for i in range (0, len(a), 1):
		l1.append(float(a[i]))
	data.append(l1) 
	l = f.readline()
	

rows = len(data)
columns = len(data[0])
f.close()


# Read train file

 
f = open(sys.argv[1], 'r')
labels = {}
labels_len = [0,0]
l = f.readline()

while(l!=''):
	a = l.split()
	labels[int(a[1])] = int(a[0])
	labels_len[int(a[0])] +=1
	l = f.readline()
	
f.close()


# Find mean 

m0 = []
m1 = []

for i in range (0, rows, 1):
	if (labels.get(i) != None and labels[i] == 0):
		for j in range(0, columns, 1):
			m0.append(0.01)
			m0[j] = m0[j] + data[i][j]
	elif(labels.get(i) != None and labels[i] == 1):
		for j in range(0, columns, 1):
			m1.append(0.01)
			m1[j] = m1[j] + data[i][j]	


for i in range(0, columns, 1):
	m0[i] = m0[i]/labels_len[0]
	m1[i] = m1[i]/labels_len[1]
	

# Standard Deviation

sd0 = []
sd1 = []

for i in range(0, columns, 1):
	sd0.append(0)
	sd1.append(0)

for i in range(0, rows, 1):
	if ( labels.get(i) != None and labels[i] == 0):
		for j in range(0, columns, 1):
			sd0[j] = sd0[j] + ( data[i][j] - m0[j])**2
	elif (labels.get(i) != None and labels[i] == 1):
		for j in range (0, columns, 1):
			sd1[j] = sd1[j] + ( data[i][j] - m1[j])**2

for i in range (0, columns, 1):
	sd0[i] = math.sqrt(sd0[i]/labels_len[0])
	sd1[i] = math.sqrt(sd1[i]/labels_len[1])


# Unlabeled points

for i in range (0, rows, 1):
	if (labels.get(i) == None):
		d0 = 0
		d1 = 0
		for j in range(0, columns, 1):
			d0 = d0 + ((data[i][j] - m0[j])/sd0[j])**2
			d1 = d1 + ((data[i][j] - m1[j])/sd1[j])**2
		if (d0<d1):
			print("0", i, end = '\n')
		else:
			print("1", i, end = '\n')