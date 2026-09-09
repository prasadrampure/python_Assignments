import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,confusion_matrix, classification_report,f1_score,precision_score
from sklearn.preprocessing import StandardScaler

border = "-"*50
# Step 1 -> Load The Dataset

print(border)
print("Step 1 -> Load The Dataset")
print(border)

data = pd.read_csv("Loan_Default.csv")

print("First 5 Records :")
print(data.head())

# Step 2 -> Data Analysis(EDA)

print(border)
print("Step 2 -> Data Analysis(EDA)")
print(border)

print("Shape of Dataset :")
print(data.shape)

print("Column Names :")
print(data.columns)

print("Check Missing Values :")
print(data.isnull().sum())

print("Encode Catagorical Variables")

data["PreviousDefault"] = data["PreviousDefault"].map({"Yes" : 1, "No" : 0})
print(data["PreviousDefault"].head())

data["HomeOwnership"] = data["HomeOwnership"].map({"Own" : 1, "Rent" : 0, "Mortgage" : 2})
print(data["HomeOwnership"].head())

# Step 3 -> Separate Independent & Dependent Variables

X = data[["Age","Income","LoanAmount","CreditScore","EmploymentYears","ExistingLoans","MonthlyDebt","LoanTerm","PreviousDefault","HomeOwnership"]]
Y = data["Default"]

print("Input Features :")
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

# Step 5 -> Feature Scaling

print(border)
print("Step 5 -> Feature Scaling")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
x_test_scaled = scalar.transform(X_test)

print("Scaled Data :")
print(X_train_scaled[:5])

# Step 6 -> Create The Model

print(border)
print("Step 6 -> Create The Model")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(100,50,25),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print("Train The Model ")

model = model.fit(X_train_scaled,Y_train)
print("Model trained Sucessfully")

Y_pred = model.predict(x_test_scaled)

Accuracy = accuracy_score(Y_test,Y_pred) 
print("Accuracy :",Accuracy)

Confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :",Confusion)

Report = classification_report(Y_test,Y_pred)
print("Classification Report :",Report)

Score = f1_score(Y_test,Y_pred)
print("F1 Score :",Score)

precision = precision_score(Y_test,Y_pred)
print("Precision :",precision)

# Step 7 -> Plot Loss Curve

print(border)
print("Step 7 -> Plot Loss Curve")
print(border)

plt.plot(model.loss_curve_)

plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Marvellous Loss Curve")
plt.show()