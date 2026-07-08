def Divisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    No = int(input("Enter a number"))
    Ret = Divisible(No)
    if Ret:
        print("True")
    else:
        print("False")
    

if __name__ == "__main__":
    main()