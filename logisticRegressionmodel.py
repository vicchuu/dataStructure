

import numpy as np


class LogisticRegression:
    def __init__(self, learningRate,totalIterations):
        self.learningRate=learningRate
        self.totalIteratins=totalIterations
    def fit(self,X,Y):
        self.m,self.n=X.shape

        self.weight=np.zeros(self.n)
        self.bias=0
        self.X=X
        self.Y=Y


        for _ in range(self.totalIteratins):
            self.updateWeights()



    def predict(self,X):
        #same as sigmoid function

        y_pred=1/(1+np.exp(-(X.dot(self.weight)+self.bias)))    #y=mx+c

        return np.where(y_pred>0.5,1,0)
    def updateWeights(self):

        #sigmoid function
        ypredicted=1/(1+np.exp(-(self.X.dot(self.weight)+self.bias)))    #y=mx+c

        #Gradient descent (optimizn algo for low loss function
        dw= (1/self.m)*np.dot(self.X.T,(ypredicted-self.Y))

        db=(1/self.m)*np.dot(ypredicted,self.Y)

        #updating new weight and bias

        self.weight = self.weight-self.learningRate * dw
        self.bias = self.bias - self.learningRate * db
