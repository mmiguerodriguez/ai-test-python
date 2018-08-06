import mnist
import numpy as np

class Task:
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.train_x = mnist.train_images().reshape(60000, 784, 1)[0:50000]
        self.train_y = np.eye(10)[mnist.train_labels()].reshape(60000, 10, 1)[0:50000]
        self.test_x = mnist.test_images().reshape(10000, 784, 1)
        self.test_y = mnist.test_labels().reshape(10000, 1)
    
    def train_input(self):
        indices = np.random.choice(self.train_x.shape[0], self.batch_size)
        return list(self.train_x[indices]), list(self.train_y[indices])
    
    def test_input(self):
        #indices = np.random.choice(self.test_x.shape[0], self.batch_size)
        index = np.random.randint(self.test_x.shape[0])
        return list(self.test_x[index]), list(self.test_y[index])