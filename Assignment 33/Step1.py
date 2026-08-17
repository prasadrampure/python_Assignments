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

def main():
    Regression("Advertising.csv")

if __name__ == "__main__":
    main()