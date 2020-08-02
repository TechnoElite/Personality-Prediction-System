import pandas as pd
from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import neighbors






data =pd.read_csv('train dataset.csv')
array = data.values

for i in range(len(array)):
    if array[i][0]=="Male":
        array[i][0]=1
    else:
        array[i][0]=0


df=pd.DataFrame(array)

maindf =df[[0,1,2,3,4,5,6]]

mainarray=maindf.values

print (mainarray)


temp=df[7]
train_y =temp.values
# print(train_y)
# print(mainarray)


for i in range(len(train_y)):
    train_y[i] =str(train_y[i])



mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
mul_lr.fit(mainarray, train_y)




maindf =df[[0,1,2,3,4,5,6]]

mainarray=maindf.values
data1 =pd.read_csv('quizans.csv')
array = data1.values

temp = []
temp1= []
k=2

for i in range(0,5):
    N=k+5
    
    for j in range(k,N):
        temp.append(array[0][j])
        
        
    
    temp1.append(round((sum(temp)/25)*10))
    k=N
    temp=[]
    array[0][2+i]=temp1[i]
for i in range(len(array)):
    if array[i][0]=="Male":
        array[i][0]=1
    else:
        array[i][0]=0
    
df1=pd.DataFrame(array)

testdf =df1[[0,1,2,3,4,5,6]]
maintestarray=testdf.values
print(maintestarray)
y_pred = mul_lr.predict(maintestarray)
for i in range(len(y_pred)) :
    y_pred[i]=str((y_pred[i]))
DF = pd.DataFrame(y_pred,columns=['Predicted Personality'])
DF.index=DF.index+1
DF.index.names = ['Person No']
DF.to_csv("try.csv")
