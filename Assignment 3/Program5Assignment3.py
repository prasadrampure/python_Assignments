def SumDigit(No):

    Sum = 0
    while(No != 0):
        SumDigit = No % 10
        Sum = Sum * 10 + SumDigit 
        No = No // 10
    if No == Sum:
        return True
    else:
        return False
    

def main():
    No = int(input("Enter a number:"))
    Ret = SumDigit(No)
    if Ret == True:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
    
if __name__ == "__main__":
    main()