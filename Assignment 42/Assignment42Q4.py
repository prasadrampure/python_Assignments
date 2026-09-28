import numpy as np

x = 5
weight = 0.5
bias = 0.2
Target = 5
Learning_Rate = 0.1

Prediction = (x * weight) + bias

Error = Target - Prediction

Old_weight = weight

weight = weight + (Learning_Rate * Error * x)

print("Input :",x)
print("Old Weight :",Old_weight)
print("Target :",Target)
print("Prediction :",Prediction)
print("Error :",Error)
print("Updated Weight :",weight)