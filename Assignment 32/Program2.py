import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    border = "-"*50
    Data = {
            "Name": ["Amit","Sagar","Pooja"],
            "Gender": ["Male", "Male", "Female"],
            "Math": [85,90,78],
            "Science": [92,88,80],
            "English": [75,85,82]
        }
    
    df = pd.DataFrame(Data)

    print(border)
    print("Min-Max Scaling")
    print(border)   

    scaler = MinMaxScaler()

    df["Math"] = scaler.fit_transform(df[["Math"]])
    print(df)

    print(border)
    print("One-Hot Encoding")
    print(border)

    df = pd.get_dummies(df, columns=["Gender"], dtype=int)
    print(df)

if __name__ == "__main__":
    main()