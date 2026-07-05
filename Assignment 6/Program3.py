Max = lambda No1,No2 : No1 > No2

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input('Enter second number:'))
    Ret = Max(No1,No2)
    if Ret == True:
        Ret = No1
    else:
        Ret = No2
    print("Maximum Num is:",Ret)


if __name__ == "__main__":
    main()