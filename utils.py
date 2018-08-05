import numpy as np

def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))

def sigmoid_prime(Z):
    return (1 - sigmoid(Z)) * sigmoid(Z)
