import itertools
import numpy as np
import matplotlib.pyplot as plt
from utils import sigmoid, sigmoid_prime
import os

class Agent:
    def __init__(self, weights, biases, learning_rate, regularization):
        self.Ws = weights
        self.Bs = biases
        self.learning_rate = learning_rate
        self.regularization = regularization
        self.costs = []
        self.accuracies = []

    def train(self, batch_x, batch_y):
        gradients = []

        for X, Y in zip(batch_x, batch_y):
            self.Xs = [X]
            self.Y = Y
            self.forward_pass()
            self.costs.append(self.compute_cost())
            gradients.append(self.backward_pass())
        
        dCdWs, dCdBs = np.average(gradients, axis=0) * self.learning_rate
        self.Ws = [W - dW for W, dW in zip(self.Ws, dCdWs)]
        self.Bs = [B - dB for B, dB in zip(self.Bs, dCdBs)]

    def test(self, x, y):
        self.Xs = [x]
        self.forward_pass()
        self.accuracies.append(y == np.argmax(self.Xs[-1]))

    def forward_pass(self):
        self.Zs = []
        for i, (W, B) in enumerate(zip(self.Ws, self.Bs)):
            self.Zs.append(np.dot(W, self.Xs[i]) + B)
            self.Xs.append(sigmoid(self.Zs[i]))

    def backward_pass(self):
        dCdZ = ((self.Xs[-1] - self.Y) * sigmoid_prime(self.Zs[-1])).T
        dCdWs = [dCdZ * self.Xs[-2] + self.Ws[-1].T * self.regularization]
        dCdBs = [dCdZ]

        for i in range(len(self.Ws) - 1, 0, -1):
            dZdZ = self.Ws[i] * sigmoid_prime(self.Zs[i - 1]).T #dZdX * dXdZ
            dCdZ = np.dot(dCdZ, dZdZ)
            dCdW = dCdZ * self.Xs[i - 1] + self.Ws[i - 1].T * self.regularization #dCdZ * dZdW
            dCdWs.append(dCdW)
            dCdBs.append(dCdZ)

        dCdWs = [dCdW.T for dCdW in dCdWs[::-1]]
        dCdBs = [dCdB.T for dCdB in dCdBs[::-1]]
        return dCdWs, dCdBs

    def compute_cost(self):
        return sum((self.Y - self.Xs[-1]) ** 2) / 2

    def save(self):
        path = 'data/{}'.format(self.exp_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        np.savez(path, sizes=self.sizes, Ws=self.Ws, Bs=self.Bs)

    def restore(self):
        npzfile = np.load('data/{}.npz'.format(self.exp_name))
        self.sizes, self.Ws, self.Bs = [item for _, item in npzfile.items()]