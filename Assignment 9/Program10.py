def SumDigit(No):
    Sum = 0
    Digit = No
    while(No!=0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No//20
    return Sum


def main():
    No = int(input("Enter a number :"))
    Ret = SumDigit(No)
    print("Sum of digit is :",Ret)

if __name__ == "__main__":
    main()