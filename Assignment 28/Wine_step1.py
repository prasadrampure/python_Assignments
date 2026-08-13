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

def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()