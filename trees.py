import matplotlib.pyplot as plt

import LinearRegressionModel as lrm

import logisticRegressionmodel as lreg
import numpy as np
import pandas as ps




"""Linear Regression """
#
# dataset=ps.read_csv("Salary_Data.csv")
#
# X=dataset.iloc[:,:-1].values
# Y=dataset.iloc[:,1].values
#
# #print(X.shape,Y.shape)
# #print(X)
# print("Y :",Y)
#
# from sklearn.model_selection import train_test_split
#
#
# xtrain,xtest,ytrain,ytest=train_test_split(X,Y, test_size=0.2,random_state=3)
#
# modelReg=lrm.LinearRegression(learningCurve=0.002,noofiterations=10000)
#
# #print(xtrain.shape , ytrain.shape)
# modelReg.fit(xtrain,ytrain)
# newY=modelReg.predict(xtest)
#
# import matplotlib.pyplot as plt
#
# plt.scatter(xtest,ytest,color="red")
# plt.plot(xtest,newY,"g--")
#
# plt.xlabel("x value")
# plt.ylabel("Y label")
# plt.show()

"""Logistics Regression"""

dataset=ps.read_csv("diabetes.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
# print(X[5,:])
# print(Y)
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler



for a in range(100,0,-1):
    if(a==90):
        a=10
    print(a)
sc=StandardScaler()
newXValue=sc.fit_transform(X)


xtrain,xtest,ytrain,ytest=train_test_split(newXValue,Y,test_size=0.3,random_state=3)



print(xtrain.shape,ytrain.shape)
print(xtest.shape,ytest.shape)
regeress=lreg.LogisticRegression(learningRate=0.001,totalIterations=100)

regeress.fit(xtrain,ytrain)

testPredicted=regeress.predict(xtest)
trainPredicted=regeress.predict(xtrain)

from sklearn.metrics import accuracy_score

print(accuracy_score(trainPredicted,ytrain))


print(accuracy_score(testPredicted,ytest))

print(regeress.weight ,  regeress.bias , regeress.learningRate)

# plt.scatter(xtest,ytest,color="green")
# plt.plot(xtest,testPredicted,color="red")
# plt.title("Logistic Regressoion")
# plt.show()






