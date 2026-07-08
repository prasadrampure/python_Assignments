def CountDigit(No):
    Count = 0
    Digit = No
    while(No!=0):
        Digit = No % 10
        Count = Count+1
        No = No//10
    return Count

    

def main():
    No = int(input("Enter a number :"))
    Ret = CountDigit(No)
    print("Count is :",Ret)

if __name__ == "__main__":
    main()
