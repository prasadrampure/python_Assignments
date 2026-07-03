def iDigit(Num):
    Sum = 0
    while(Num != 0):
        iDigit = Num % 10
        Sum = Sum + 1
        Num = Num // 10
    return Sum


def main():
    Num = int(input("Enter a number:"))
    Ret = iDigit(Num)
    print("Count of Digit is :", Ret)


if __name__ == "__main__":
    main()