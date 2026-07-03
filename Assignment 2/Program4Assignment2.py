def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():

    No = int(input("Enter a number:"))
    Ret = CheckEven(No)
    if (Ret):
        print("Number is Even")

    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()