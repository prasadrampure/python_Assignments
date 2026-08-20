import pandas as pd
from sklearn.linear_model import LinearRegression

def MarvellousRegression():
    border = "-"*40

    Data = {
        "StudyHours" : [1,2,3,4,5],
        "SleepHours" : [7,6,7,6,8],
        "Marks" : [50,55,60,65,70]
    }

    df = pd.DataFrame(Data)

    print(border)
    print("Dataset : ")
    print(border)

    print(df)

    print(border)

    X = df[["StudyHours", "SleepHours"]]
    Y = df["Marks"]

    model = LinearRegression()

    model = model.fit(X,Y)

    print("Model trained successfully")

    print(border)

    print("Coefficent of X :",model.coef_[0])
    print("Coefficent of Y :",model.coef_[1])

    print(border)

    print("Intercept :",model.intercept_)
    
def main():
    MarvellousRegression()

if __name__ == "__main__":
    main()