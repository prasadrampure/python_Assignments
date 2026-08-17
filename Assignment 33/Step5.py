import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def Regression(DataPath):
    border = "-"*50

    print(border)
    print("Step 1 : Load The Data")
    print(border)

    df = pd.read_csv(DataPath)

    print(df.head())

    print(border)
    print("Step 2 : Clean & Manipulate Data")
    print(border)

    # Remove unwanted columns
    print("Remove Unwanted Column")
    df = df.drop(columns=["Unnamed: 0"])
    print(df.head())

    print(border)

    #Check missing values
    print("Check Missing Values")
    print(df.isnull().sum())

    print(border)

    #Separte Independent & Dependent Variabels
    print("Separte Independent & Dependent Variabels")

    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Independent Variable :")
    print(X.head())

    print("Dependent Variable :")
    print(Y.head())

    print(border)

    #Split the Data
    print("Split The Data")

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Training Data :",X_train.shape)
    print("Testing Data :",Y_train.shape)

    print(border)
    print("Step 3 : Train The Data")
    print(border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    print("Model trained Successfully")

    print(border)
    print("Test The Data")
    print(border)

    Y_pred = model.predict(X_test)

    print("Predicted Sales :")
    print(Y_pred[:5])

    print(border)
    print("Step 5 : Display Predicted Values & Expected Values :")
    print(border)

    print("Expected Answers :")
    print(Y_test[:5])

    print("Predicted Answers :")
    print(Y_pred[:5])

def main():
    Regression("Advertising.csv")

if __name__ == "__main__":
    main()