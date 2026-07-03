def Factorial(No):
    Num = 1

    for i in range(1, No+1):
        Num = Num * i
    return Num

def main():

    No = int(input("Enter a number:"))
    Ret = Factorial(No)
    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()