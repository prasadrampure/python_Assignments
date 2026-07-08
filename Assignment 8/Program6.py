def CheckPositive(No):
    if(No>0):
        return True
    else:
        return False

def main():
    No = int(input("Enter a number :"))
    

    Ret = CheckPositive(No)
    if Ret == True:
        print("Number is positive")
    else:
        print("Number is negative")

if __name__ == "__main__":
    main()