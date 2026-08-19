import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

def SalaryPredictor():
    border = "-"*40

    Data = {
        "Experience" : [1,2,3,4,5],
        "Salary" : [20000,25000,30000,35000,40000]
    }

    df = pd.DataFrame(Data)

    print(border)
    print("Dataset")
    print(border)

    print(df)

    X = df[["Experience"]]
    Y = df["Salary"]

    model = LinearRegression()

    model = model.fit(X,Y)

    print(border)
    print("LinearRegression Model trained")

    print(border)

    print("Slope :",model.coef_[0])
    print("Intercept :",model.intercept_)

    print(border)

    Experience = pd.DataFrame({"Experience" : [6]})

    predictedSalary = model.predict(Experience)

    print("Predicted Salary for 6 year experiance :" +str(int(predictedSalary[0])))

    print(border)

    plt.scatter(X,Y,label = "Actual Data")

    plt.plot(
        X,
        model.predict(X),
        label = "Regrassion Line"
    )

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.legend()
    plt.show()
            
def main():
    SalaryPredictor()

if __name__ == "__main__":
    main()