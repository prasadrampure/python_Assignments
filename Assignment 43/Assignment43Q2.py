from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

border = "-"*100
print(border)

x =[
    [25000,600,200000,10000,0],
    [40000,700,300000,8000,1],
    [60000,750,500000,12000,1],
    [20000,550,150000,15000,0],
    [80000,800,700000,10000,1],
    [35000,650,250000,9000,1],
    [18000,500,100000,12000,0],
    [9000,850,800000,15000,1],
    [30000,580,200000,14000,0],
    [70000,780,600000,10000,1]
]

y = [
    0,1,1,0,1,
    1,0,1,0,1
]

print("X :",x)
print(border)
print("Y :",y)

scalar = StandardScaler()

x_scaled = scalar.fit_transform(x)

print(border)
print("Scaled x :",x_scaled)

X_train,X_test,Y_train,Y_test = train_test_split(
    x_scaled,
    y,
    random_state=42,
    test_size=0.3
)

model = MLPClassifier(
    hidden_layer_sizes=(4,8),
    activation="relu",
    max_iter=1000,
    random_state=42
)

model = model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
print(border)
print("Predicted Output :",Y_pred)

Accuracy = accuracy_score(Y_test,Y_pred)
print(border)
print("Accuracy :",Accuracy)

new_applicant = [[55000,720,400000,10000,1]]

new_applicant_scaled = scalar.transform(new_applicant)

prediction = model.predict(new_applicant_scaled)

print(border)
print("New Apllicant :",new_applicant)
print("Prediction :",prediction)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")