import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def WineClassifier(DataPath):
    border = "-"*50

    print(border)
    print("step 1 : Get the dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print("Data read succesfully")

    print(border)
    print("Clean the data")
    print(border)

    df.dropna(inplace=True)

    print("Shape of Dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Total Column :",df.shape[1])

    X = df.drop("Class", axis=1)
    Y = df["Class"]
    
    print("Input Data :",X.shape)
    print("Output Data",Y.shape)

    print(border)
    print("Train the data")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Traning Data :",X_train.shape)
    print("Testing Data :",X_test.shape)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)

    print("Model train succesfully")

def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()