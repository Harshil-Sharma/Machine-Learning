import sys
from math import sqrt
from sklearn import svm
import random
from sklearn.model_selection import cross_val_score

def dotProduct(w, x):
    dp = 0.0
    for wi, xi in zip(w, x):
        dp += wi * xi
    return dp

def sign(x):
    if(x > 0):
        return 1
    elif(x < 0):
        return -1
    return 0

datafile = sys.argv[1]
f=open(datafile)
merged_data=[]
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    merged_data.append(l2)
    l=f.readline()


f.close()


labelfile = sys.argv[2]
f=open(labelfile)
trainlabels= {}
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels[int(a[1])] = int(a[0])
    l=f.readline()
data=[]
testdata=[]

mv=[]
for i in range(0,len(merged_data),1):
    if(trainlabels.get(i)==None):
        testdata.append(merged_data[i])
        mv.append(i)
    else:
        data.append(merged_data[i])

noRows=len(data)
noCols =len(data[0])
labels=list(trainlabels.values())
dataSets=data
testDataSets=testdata

k = int(sys.argv[3])

w = []
for i in range(0, k, 1):
    w.append([]) 
    for j in range(0, noCols, 1):
        w[i].append(random.uniform(-1, 1))
        # w[i][j] = random.uniform(-1, 1)
    
# print ("random w " + str(w))
    
z = [] 
for i, data in enumerate(dataSets):
    z.append([])
    for j in range(0, k, 1):
        # z[i][j] = sign(dotProduct(w[j], data))
        z[i].append(sign(dotProduct(w[j], data)))
        
        
z1 = []  
for i, data in enumerate(testDataSets):
    z1.append([])
    for j in range(0, k, 1):
        # z[i][j] = sign(dotProduct(w[j], data))
        z1[i].append(sign(dotProduct(w[j], data)))




print('\n  RandomHyperPlane Data:  \n')
model = svm.SVC(kernel='linear', C=0.001, gamma=1)
model.fit(z, labels)
training_labels = model.predict(z)
    
    
scores = cross_val_score(model, z, labels, cv=5)
scores[:]= [1-x for x in scores]
print("mean error for new features data: ",scores.mean())

p_labels = model.predict(z1)

#print('\n  Using_RandomHyperPlanes \n')
with open('Predicted_Labels_Using_RandomHyperPlanes', 'w') as out:
    for i in range(len(p_labels)):
        out.write(str(int(p_labels[i])) + ' ' + str(i) + '\n')
        print(int(p_labels[i]), mv[i])

print('\n Orignal Data:  \n')
svm_model = svm.SVC(kernel='linear', C=1.0, gamma=1)
svm_model.fit(dataSets, labels)
p_labels = svm_model.predict(testDataSets)

scores_o = cross_val_score(svm_model, dataSets, labels, cv=5)
scores_o[:]=[1-x for x in scores_o]
print("mean error for orginal data: ",scores_o.mean())

with open('Predicted_Labels_Using_OriginalDataPoints', 'w') as out:
    for i in range(len(p_labels)):
        out.write(str(int(p_labels[i])) + ' ' + str(i) + '\n')
        print(int(p_labels[i]), mv[i])


