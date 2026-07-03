from Calculation import *

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter Second number:"))

    Ret = Addition(No1, No2)
    print("Addition is :",Ret)

    Ret = Subtraction(No1, No2)
    print("Subtraction is :",Ret)

    Ret = Multiplication(No1, No2)
    print("Multiplication is :",Ret)

    Ret = Division(No1, No2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()