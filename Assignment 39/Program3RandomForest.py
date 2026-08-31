import pandas as pd

from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score ,confusion_matrix ,f1_score ,precision_score, recall_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def main():

    # Step 1 -> Load The Dataset

    df = pd.read_csv("Fraudulent_Transaction_Detection.csv") 

    print("Shape of Dataset ",df.shape)
    print("First Few records")
    print(df.head())

    # Step 2 -> Seperate Features & Labels
    X = df.drop("Fraud", axis=1)
    Y = df["Fraud"]

    print("X Shape :",X.shape)
    print("Y Shape :",Y.shape)

    # Step 3 -> Split The Dataset For Training & Testing

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )

    print("Dataset Split Successfully")

    # Step 4 -> Scale the Features

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.fit_transform(X_test)

    # Step 5 -> Create The Model

    model = RandomForestClassifier(
        random_state=42,
        n_estimators=10
        )

    # Step 6 -> Train the model

    model = model.fit(X_train,Y_train)
    print("model trained Successfully")

    # Step 7 -> Test the model

    Y_pred = model.predict(X_test)

    # Step 8 -> Evaluate the model

    Accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy : ",Accuracy)

    print("Confusion Matrix :")
    print(confusion_matrix(Y_test,Y_pred))

    print('Precision Score :')
    print(precision_score(Y_test,Y_pred))

    print("Recall Score :")
    print(recall_score(Y_test,Y_pred))

    print("f1 Score :")
    print(f1_score(Y_test,Y_pred))

if __name__ == "__main__":
    main()