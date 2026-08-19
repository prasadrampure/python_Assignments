from sklearn.metrics import mean_squared_error, r2_score
def ManuallyLinearRegression():
    border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print(border)
    print("Mean_X :",mean_x)
    print("Mean_Y :",mean_y)

    n = len(X)

    numerator = 0
    denominator= 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    m = numerator / denominator

    print(border)
    print("Slope(m) : ",m)   

    c = mean_y - m * mean_x

    print(border)
    print("Intercept (c) :",c)

    print(border)
    print("Predicted Y Values")
    print(border)

    Y_pred = []

    for i in range(n):
        predicted_y = m * X[i] + c
        Y_pred.append(predicted_y)

        print(
            "X :", X[i],
            "Actual Y :", Y[i],
            'Predicted Y :',predicted_y)

    print(border)
    print("Calculate MSE & R2")
    print(border)

    MSE = mean_squared_error(Y, Y_pred)

    R2 = r2_score(Y, Y_pred)

    print("MSE :",MSE)
    print("R2 :",R2)

def main():
    ManuallyLinearRegression()

if __name__ == "__main__":
    main()