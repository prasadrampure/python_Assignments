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
    
def main():
    ManuallyLinearRegression()

if __name__ == "__main__":
    main()