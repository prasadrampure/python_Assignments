largest = lambda No1,No2,No3 : 1 if (No1 > No2 and No1 > No3) else 2 if (No2 > No1 and No2 > No3) else 3

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    No3 = int(input("Enter third number:"))

    Ret = largest(No1,No2,No3)
    if (Ret == 1):
        print("No1 is Greater than No2 and No3")
    elif (Ret == 2):
        print("No2 is Greater than No1 and No3")
    else:
        print("No3 is Greater than No1 and No2")


if __name__ == "__main__":
    main()