import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler


border = '-'*50
# Step 1 -> Load The Dataset

print(border)
print("Step 1 -> Load The Dataset")
print(border)

data = pd.read_csv("Employee_Attrition.csv")

print("First 5 Records :")
print(data.head())

# Step 2 -> Data Analysis(EDA)

print(border)
print("Step 2 -> Data Analysis(EDA)")
print(border)

print("Shape Of Dataset :")
print(data.shape)

print("Column Names :")
print(data.columns)

print("Check Missing Values :")
print(data.isnull().sum())

print("Convert Catagorical feature into Numerical")

data["OverTime"] = data["OverTime"].map({"Yes" : 1, "No" : 0})
print(data["OverTime"].head())

data["Attrition"] = data["Attrition"].map({"Yes" : 1, "No" : 0})
print(data["Attrition"].head())

# Step 3 -> Separate independent & Dependent Variable

print(border)
print(" Step 3 -> Separate independent & Dependent Variable")
print(border)

X = data[["Age","MonthlyIncome","YearsAtCompany","TotalWorkingYears","DistanceFromHome","JobSatisfaction","WorkLifeBalance","OverTime","NumCompaniesWorked","TrainingTimesLastYear"]]
Y = data["Attrition"]

print("input Features :")
print(X.head())

print("Target :")
print(Y.head())

# Step 4 -> Train Test Split

print(border)
print("Step 4 -> Train Test Split")
print(border)

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("Training input shape :",X_train.shape)
print("Testing input shape :",X_test.shape)
print("Training Output shape :",Y_train.shape)
print("Testing Output shape :",Y_test.shape)

# Step 5 -> Feature Scaling

print(border)
print("Step 5 -> Feature Scaling")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data :")
print(X_test_scaled[:5])

# Step 6 -> Crate Model

print(border)
print('Step 6 -> Crate Model')
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Train The Model :")

model = model.fit(X_train_scaled,Y_train)

print("Model Trained Successfully")

# Step 7 -> Model Evaluation

print(border)
print("Step 7 -> Model Evaluation")
print(border)

Y_train_pred = model.predict(X_train_scaled)

Accuracy = accuracy_score(Y_train,Y_train_pred)
print("Traning Accuracy :",Accuracy)

Y_pred = model.predict(X_test_scaled)

Accuracy = accuracy_score(Y_test,Y_pred)
print("Testing Accuracy :",Accuracy)

confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :",confusion)

# Step 8 -> Plot Loss Curve

print(border)
print("Step 8 -> Plot Loss Curve")
print(border)

plt.plot(model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("Marvellous Loss Curve")
plt.show()
