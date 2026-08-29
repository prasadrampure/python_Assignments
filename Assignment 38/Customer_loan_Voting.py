import pandas  as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    border = "-"*50

    print(border)
    print("Step 1 : Load the Dataset")
    print(border)

    df = pd.read_csv("Customer_Loan_Approval.csv")

    print("Shape of Dataset :",df.shape)

    print("First 5 Records")
    print(df.head())

    print(border)
    print("Step 2 : separate input & output Variabels")
    print(border)

    X = df.drop("LoanApproved", axis=1)
    Y = df["LoanApproved"]

    print("X Shape :",X.shape)
    print("Y Shape :",Y.shape)

    print(border)
    print("Step 3 : Split Dataset For Traning & Testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Records :", X_train.shape[0])
    print("Testing Records  :", X_test.shape[0]) 

    print("Dataset Split successfully")

    print(border)
    print("Step 4 : Feature Scaling")
    print(border)

    scalar = StandardScaler()

    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    print("Feature Scaling completed")

    print(border)
    print("Step 5 : Train Logistic Model")
    print(border)

    model_log = LogisticRegression(max_iter=1000)
    model_log.fit(X_train,Y_train)

    Y_pred_log = model_log.predict(X_test)
    acc_log = accuracy_score(Y_test,Y_pred_log)

    print("Logistic Accuracy :",acc_log)

    print(border)
    print("Step 6 : Train DesitionTree Model")
    print(border)

    model_tree = DecisionTreeClassifier(random_state=42)
    model_tree.fit(X_train,Y_train)

    Y_pred_tree = model_tree.predict(X_test)
    acc_tree = accuracy_score(Y_test,Y_pred_tree)

    print("Desition tree Accuracy :",acc_tree)

    print(border)
    print("Step 7 : Train KNN Model")
    print(border)

    model_knn = KNeighborsClassifier(n_neighbors=5)
    model_knn.fit(X_train,Y_train)

    Y_pred_knn = model_knn.predict(X_test)
    acc_knn = accuracy_score(Y_test,Y_pred_knn)

    print("KNN Accuracy :",acc_knn)

    print(border)
    print("Step 8 : Hard Voting")
    print(border)

    hard_model = VotingClassifier(
        estimators=[
            ("logistic",LogisticRegression(max_iter=1000)),
            ("tree",DecisionTreeClassifier(random_state=42)),
            ("knn",KNeighborsClassifier(n_neighbors=5))
        ],
        voting='hard'
    )

    hard_model.fit(X_train,Y_train)

    Y_pred_hard = hard_model.predict(X_test)

    acc_hard = accuracy_score(Y_test,Y_pred_hard)
    print("Hard Voting Accuracy :",acc_hard)

    print(border)
    print("Step 9 : Soft Voting")
    print(border)

    soft_model = VotingClassifier(
        estimators=[
            ("logistic",LogisticRegression(max_iter=1000)),
            ("tree",DecisionTreeClassifier(random_state=42)),
            ("knn",KNeighborsClassifier(n_neighbors=5))
        ],
        voting='soft'
    )

    soft_model.fit(X_train,Y_train)

    Y_pred_soft= soft_model.predict(X_test)

    acc_soft = accuracy_score(Y_test,Y_pred_soft)
    print("Soft Voting Accuracy :",acc_soft)

if __name__ == "__main__":
    main()
