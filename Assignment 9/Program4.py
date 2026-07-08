def SumFactor(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum += i
    return Sum

def main():
    No = int(input("Enter a number :"))
    Ret= SumFactor(No)
    print("Sum of Factorial is :",Ret)

if __name__ == "__main__":
    main()
