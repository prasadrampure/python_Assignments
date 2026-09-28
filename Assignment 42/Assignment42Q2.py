import numpy as np
import matplotlib.pyplot as plt

# Input Values
x = np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])

# Sigmoid Activation function
sigmoid = 1 / (1 + np.exp(-x))

# relu Activation function
Relu = np.maximum(0,x)

# tanh Activation function
tanh = np.tanh(x)

print("Input :",x)
print("Sigmoid :",sigmoid)
print("ReLU :",Relu)
print("tanh :",tanh)

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, Relu, label="ReLU")
plt.plot(x, tanh, label="tanh")

plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Activation Function")
plt.legend()

plt.show()