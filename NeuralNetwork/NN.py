import matplotlib as plt
import numpy as np



class NeuralNetwork(object):

    def __init__(self):
        #HyperParameters
        self.inputLayers = 2
        self.outputLayers = 1
        self.hiddenLayerSize = 3

        #Weights
        self.W1 = np.random.randn(self.inputLayers, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayers)

    def sigmoid(self, z):
        return 1/(1 + np.exp(-z))

    def sigmoidPrime(self, z):
        return np.exp(-z)/((1 + np.exp(-z))**2)

    def forward(self, X):
        self.Z1 = np.dot(X, self.W1)
        self.a = self.sigmoid(Z1)
        self.Z2 = np.dot(self.a, self.W2)
        self.yhat = self.sigmoid(Z2)
        return yHat

    def cost(self, X, y):
        self.yhat = self.forward(X)
        J = 0.5*sum((y - self.yhat)**2)
        return J

    def costPrime(self, X, y):
        self.yhat = self.forward(X)

        delta3 = np.multiply(-(y - self.yhat), self.sigmoidPrime(self.Z2))
        W2prime = np.dot(self.a.T, delta3)

        delta2 = np.dot(delta3, self.W2.T)*sigmoidPrime(self.Z1)
        W1prime = np.dot(X.T, delta2)

        return W1prime, W2prime
