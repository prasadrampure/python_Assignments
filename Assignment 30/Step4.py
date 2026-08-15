import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def PlayPredictor(DataPath):
    border = "-"*50

    print(border)
    print("Get Dataset From csv File")
    print(border)

    df = pd.read_csv(DataPath)

    print("Data reads sucessfully")

    print(border)
    print("Clean the data")
    print(border)

    df.dropna(inplace=True)

    print("Shape of Dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Total Colouns :",df.shape[1])

    print(border)
    print("Convert String Data into Numerical Data")
    print(border)

    Encoder = LabelEncoder()

    df["Wether"] = Encoder.fit_transform(df["Wether"])
    df["Temperature"] = Encoder.fit_transform(df["Temperature"])
    df["Play"] = Encoder.fit_transform(df["Play"])

    print("Data converted successfully")

    print(border)
    print("Train the model")
    print(border)

    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Traning Data :",X_train.shape)
    print("Testing Data :",X_test.shape)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)

    print("Model train Succesfully")

    print(border)
    print("Test the data")
    print(border)

    Y_pred = model.predict(X_test)

    print("Predicted Data :",Y_pred)
    print("Actual data :",Y_test.values)

def main():
    PlayPredictor("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()