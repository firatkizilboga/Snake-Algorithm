import numpy as np
import time
class NeuralNetwork():
    def __init__(self):
        self.layer1=np.random.rand(9,9)
        self.layer2=np.random.rand(9,6)
        self.layer3=np.random.rand(6,3)
        self.layer4=np.random.rand(3,3)
        self.layers=[self.layer1,self.layer2,self.layer3,self.layer4]
        self.weights=[]
        for i in self.layers:
            self.weights.append(i.tolist())
    def load_weights(self,weights):
        self.layer1=weights[0]
        self.layer2=weights[1]
        self.layer3=weights[2]
        self.layer4=weights[3]
        self.layers=[self.layer1,self.layer2,self.layer3,self.layer4]
        self.weights=[]
        for i in self.layers:
            self.weights.append(i)
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    def predict(self,i):
        xw=np.array(i).ravel()
        for layer in self.layers:
            xw=np.dot(xw,layer)
        xw=xw.reshape(-1,1).tolist()
        if xw.index(max(xw))==0:
            output="w"
        if xw.index(max(xw))==1:
            output="a"
        if xw.index(max(xw))==2:
            output="d"
        return output