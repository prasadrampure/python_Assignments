import pandas as pd

from sklearn.linear_model import LinearRegression

def MarvellousRegression():
    border = "-"*40

    Data = {
        "StudyHours" : [1,2,3,4,5],
        "Marks" : [50,55,60,65,70]
    }

    df = pd.DataFrame(Data)

    print(border)
    print("DataSet")
    print(border)

    print(df)

    print(border)

    X = df[["StudyHours"]]
    Y = df["Marks"]

    model = LinearRegression()

    model = model.fit(X,Y)

    print("Model trained successfully")

    print(border)

    print("Coefficient :",model.coef_[0])

    print(border)
    
    print("Intercept :",model.intercept_)

    print(border)

def main():
    MarvellousRegression()

if __name__ == "__main__":
    main()