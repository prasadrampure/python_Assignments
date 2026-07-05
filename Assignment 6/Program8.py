Addition = lambda Num1,Num2 : (Num1 + Num2)


def main():
    Num1 = int(input("Enter First number:"))
    Num2 = int(input("Enter second number:"))
    Ret = Addition(Num1,Num2)
    print("Addition is :",Ret)
    
if __name__  == '__main__':
    main()