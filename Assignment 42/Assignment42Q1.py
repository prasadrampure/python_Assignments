import numpy as np

# Input Features i.e X

input = np.array([2,3])
print("X :",input)

# Weights i.e w

weights = np.array([0.4,0.6])
print("w :",weights)

# bias i.e b

bias = 0.5

# Calculate weighted sum i.e z

z = np.dot(input,weights) + bias
print("z :",z)

# Activation function (Sigmoid)

sigmoid = 1 / (1 + np.exp(-z))
print("Sigmoid :",sigmoid)