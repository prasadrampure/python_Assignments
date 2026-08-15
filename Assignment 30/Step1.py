import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def PlayPredictor(DataPath):
    border = "-"*50

    print(border)
    print("Get Dataset From csv File")
    print(border)

    df = pd.read_csv(DataPath)

    print("Data reads sucessfully")

def main():
    PlayPredictor("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()