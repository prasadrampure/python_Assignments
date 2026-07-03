def CheckOdd(No):
    if(No % 2 == 1):
        return True
    else:
        return False

def main():

    No = int(input("Enter a number:"))
    Ret = CheckOdd(No)
    if (Ret):
        print("Number is Odd")

    else:
        print("Number is Even")

if __name__ == "__main__":
    main()