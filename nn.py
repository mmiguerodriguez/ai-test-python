import itertools
import numpy as np
import matplotlib.pyplot as plt
from utils import sigmoid, sigmoid_prime
import mnist
import os

class NN():
    exp_name = 'nn5'
    learning_rate = .03
    regularization = .003

    def __init__(self):
        self.sizes = [784, 100, 30, 10]
        self.Ws = [np.random.randn(m, n) for m, n in zip(self.sizes[1:], self.sizes)]
        self.Bs = [np.random.randn(m, 1) for m in self.sizes[1:]]
        #self.restore()
        self.load_mnist()

    def run(self):
        accuracies = []

        for i in itertools.count():
            try:
                self.costs = []
                self.train()
                accuracies.append(self.test())
                print ('Epoch {}: Cost {}. Acc {}'.format(i, np.average(self.costs), accuracies[-1]))
            except KeyboardInterrupt:
                if input() == 's':
                    self.save()
                    plt.plot(accuracies)
                    plt.show(block=False)
                    time.sleep(10000)

    def sgd(self, batch_X, batch_Y):
        gradients = []

        for X, Y in zip(self.batch_X, self.batch_Y):
            self.Xs = [X]
            self.Y = Y
            self.forward_pass()
            self.costs.append(self.compute_cost())
            gradients.append(self.backward_pass())

        dCdWs, dCdBs = np.average(gradients, axis=0) * self.learning_rate
        self.Ws = [W - dW for W, dW in zip(self.Ws, dCdWs)]
        self.Bs = [B - dB for B, dB in zip(self.Bs, dCdBs)]

    def forward_pass(self):
        self.Zs = []
        for i, (W, B) in enumerate(zip(self.Ws, self.Bs)):
            self.Zs.append(np.dot(W, self.Xs[i]) + B)
            self.Xs.append(sigmoid(self.Zs[i]))

    def backward_pass(self):
        dCdZ = ((self.Xs[-1] - self.Y) * sigmoid_prime(self.Zs[-1])).T
        dCdWs = [dCdZ * self.Xs[-2] + self.Ws[-1].T * self.regularization]
        dCdBs = [dCdZ]

        for i in range(len(self.sizes) - 2, 0, -1):
            dZdZ = self.Ws[i] * sigmoid_prime(self.Zs[i - 1]).T #dZdX * dXdZ
            dCdZ = np.dot(dCdZ, dZdZ)
            dCdW = dCdZ * self.Xs[i - 1] + self.Ws[i - 1].T * self.regularization #dCdZ * dZdW
            dCdWs.append(dCdW)
            dCdBs.append(dCdZ)

        dCdWs = [dCdW.T for dCdW in dCdWs[::-1]]
        dCdBs = [dCdB.T for dCdB in dCdBs[::-1]]
        return dCdWs, dCdBs

    def test(self):
        accuracy = []

        for i in range(self.test_runnings):
            self.Xs = [self.test_images[i]]
            self.forward_pass()
            accuracy.append(self.test_labels[i] == np.argmax(self.Xs[-1]))

        return np.average(accuracy)

    def compute_cost(self):
        return sum((self.Y - self.Xs[-1]) ** 2) / 2

    def save(self):
        path = 'data/{}'.format(self.exp_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        np.savez(path, sizes=self.sizes, Ws=self.Ws, Bs=self.Bs)

    def restore(self):
        npzfile = np.load('data/{}.npz'.format(self.exp_name))
        self.sizes, self.Ws, self.Bs = [item for _, item in npzfile.items()]

    def load_mnist(self):
        self.train_images = mnist.train_images().reshape(60000, 784, 1)[0:50000]
        self.train_labels = np.eye(10)[mnist.train_labels()].reshape(60000, 10, 1)[0:50000]
        self.test_images = mnist.test_images().reshape(10000, 784, 1)
        self.test_labels = mnist.test_labels().reshape(10000, 1)

NN().run()
