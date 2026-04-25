import os
import sys
from random import random
from random import seed
import math
import numpy as np
from tensorflow.keras.datasets.mnist import load_data

(x_train, y_train), (x_test, y_test) = load_data()

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

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

# Forward propagate network weights/biased from a given input
def forward_propagate(network, input_row):
    inputs = input_row

    for layer in network:
        new_layer = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = sigmoid(activation)
            new_layer.append(neuron['output'])
        inputs = new_layer

    return inputs

# Calculate activation for a neuron, given a certain input
def activate(weights, inputs):
    # bias is last weight in list [-1]
    activation = weights[-1]

    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]

    return activation


seed(42)
network = init_network([3,1,2])
for layer in network:
    print(layer)
outputs = forward_propagate(network, [1.5,1.7,2])
print(outputs)

sample_x = x_train[1].flatten()
print(np.shape(sample_x))