import os
import sys
from random import random
from random import seed
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def init_network(structure: list):
    # Input array containing number of neurons in each layer. Starting with number of inputs, and ending with num output neurons
    # Also contains a minimum of one hidden layer

    network = []

    # idx represents which layer, i is the number of neurons in that layer
    for idx, size in enumerate(structure):
        # skip input layer
        if idx==0: 
            continue

        # +1 is there for the bias
        # initializes weights and biases for each neuron based on num neurons in previous layer, repeats for every single neuron
        layer = [{"weights": [random() for _ in range(structure[idx-1]+1)]} for _ in range(size)]
        network.append(layer)

    return network

seed(42)
network = init_network([3,1,2])
for layer in network:
    print(layer)