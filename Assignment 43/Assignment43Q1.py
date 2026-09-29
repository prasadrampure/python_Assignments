from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

border = "-"*100

X =[
    [25,500,12,1,2],
    [30,700,24,0,1],
    [45,1200,6,5,8],
    [50,1500,5,6,10],
    [28,600,18,1,1],
    [35,800,30,0,0],
    [48,1400,4,7,9],
    [52,1600,3,8,12],
    [27,550,20,0,1,],
    [24,1300,8,4,7]
]

Y = [
    0,0,1,1,0,
    0,1,1,0,1
    ]

print("X :",X)
print(border)
print("Y :",Y)

scalar = StandardScaler()

X_scaled = scalar.fit_transform(X)

print(border)
print("\nScaled X :")
print(X_scaled)
print(border)

X_train,X_test,Y_train,Y_test = train_test_split(
    X_scaled,
    Y,
    random_state=42,
    test_size=0.3
)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation="relu",
    max_iter=1000,
    random_state=42
)

model = model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
print("Predicted Output :",Y_pred)

Accuracy = accuracy_score(Y_test,Y_pred)
print(border)
print("Accuracy :",Accuracy)

new_customer = [[46,1450,5,6,9]]

new_customer_scaled = scalar.transform(new_customer)

prediction = model.predict(new_customer_scaled)

print(border)
print("New Customer :",new_customer)
print("Prediction :",prediction)

if prediction[0] == 1:
    print("Customer may leave")
else:
    print("Customer may stay")