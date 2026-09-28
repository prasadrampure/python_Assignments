import numpy as np

Actual = np.array([1,0,1,1,0])

Predicted = np.array([0.8,0.3,0.7,0.9,0.2])

print("Actual Values :",Actual)
print("Predicted Values :",Predicted)

mse = np.mean((Actual - Predicted) ** 2)
print("Mean Squared Error :",mse)

bce = -np.mean(
    Actual * np.log(Predicted) +
    (1 - Actual) * np.log(1 - Predicted)
)

print("Binary Cross entropy :",bce)