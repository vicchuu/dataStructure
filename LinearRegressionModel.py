

import numpy as np

class LinearRegression:
    def __init__(self,learningCurve, noofiterations):
        self.learningCurve=learningCurve
        self.noofiterations=noofiterations

    def fit(self,X,Y):
        #print(X.shape,Y.shape)
        self.row,self.column=X.shape


        self.weight=np.zeros(self.column)
        self.bias=0
        self.X=X
        self.Y=Y
        for a in range(self.noofiterations):
            self.updateWeights()

        return self

    def updateWeights(self):
        yprediction=self.predict(self.X)
        #print("ypredicted :",self.X.T)

        #calculate gradients
        #print((self.X.T.shape))
        # print(self.Y)
        #print("******** Y is over *****")
        #print(yprediction.shape , self.Y.shape,self.X.shape)
        #
        """In matrix multiplication , we cannot multiply both same row and column matrixes"""
        
        """we will multiply forst row * second column (m*n)
        for ex: 31*5  , 31*1   so if we transpose 5*31 then we can multiply 5*31 and 31*1 easily so transpose is used """
        wb=- ( 2 * ( self.X.T ).dot( self.Y - yprediction )  ) / self.row #slope m

        wc=-(2*np.sum(self.Y-yprediction))/self.row



        #calculate weights

        self.weight=self.weight-self.learningCurve *wb
        self.bias=self.bias=self.learningCurve*wc
        return self

    def predict(self,X):
        return X.dot(self.weight)+self.bias