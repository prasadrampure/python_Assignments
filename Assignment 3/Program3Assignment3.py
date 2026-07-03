def SumDigit(No):

    Sum = 0
    while(No != 0):
        SumDigit = No % 10
        Sum = Sum *  SumDigit 
        No = No // 10
    return Sum



def main():
    No = int(input("Enter a number:"))
    Ret = SumDigit(No)
    print("Sum of digits is :",Ret)

if __name__ == "__main__":
    main()