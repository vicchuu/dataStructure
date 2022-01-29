
import LinearRegressionModel as lrm

import numpy as np
import pandas as ps


dataset=ps.read_csv("Salary_Data.csv")

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,1].values

#print(X.shape,Y.shape)
#print(X)
print("Y :",Y)

from sklearn.model_selection import train_test_split


xtrain,xtest,ytrain,ytest=train_test_split(X,Y, test_size=0.2,random_state=3)

modelReg=lrm.LinearRegression(learningCurve=0.002,noofiterations=10000)

#print(xtrain.shape , ytrain.shape)
modelReg.fit(xtrain,ytrain)
newY=modelReg.predict(xtest)

import matplotlib.pyplot as plt

plt.scatter(xtest,ytest,color="red")
plt.plot(xtest,newY,"g--")

plt.xlabel("x value")
plt.ylabel("Y label")
plt.show()





