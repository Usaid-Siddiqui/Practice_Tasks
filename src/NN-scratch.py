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


def softmax(outputs):
    # subtract max for numerical stability (prevents exp() overflow)
    max_val = max(outputs)
    exps = [math.exp(o - max_val) for o in outputs]
    total = sum(exps)
    return [e / total for e in exps]


# Forward propagate network weights/biased from a given input
def forward_propagate(network, input_row):
    inputs = input_row

    for i, layer in enumerate(network):
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


def back_prop(network, expected_output):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []

        if i == len(network) - 1:
            for j, neuron in enumerate(layer):
                errors.append(neuron["output"] - expected_output[j])

        else:
            for j in range(len(layer)):
                error = sum(
                    network[i+1][k]['weights'][j] * network[i+1][k]['delta']
                    for k in range(len(network[i+1]))
                )
                errors.append(error)

        for j, neuron in enumerate(layer):
            neuron["delta"] = errors[j] * sigmoid_derivative(neuron["output"])


def cross_entropy_loss(output, expected):
    eps = 1e-8
    return -sum(e * math.log(o + eps) for o, e in zip(output,expected))


def sigmoid_derivative(val):
    return val * (1 - val)





#---------------------------------------------------------------------

seed(42)
network = init_network([3,1,2])
for layer in network:
    print(layer)
outputs = forward_propagate(network, [1.5,1.7,2])
print(outputs)

sample_x = x_train[1].flatten()
print(np.shape(sample_x))