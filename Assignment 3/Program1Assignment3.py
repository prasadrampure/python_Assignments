def CheckPrime(No):
    if No<= 1:
        return False
    for i in range(2,No):
        if(No % i == 0):
            return False
    else:
        return True


def main():
    No = int(input("Enter a number:"))
    Ret = CheckPrime(No)
    if(Ret):
        print("Number is prime")
    else:
        print("Number is not prime")


if __name__ == "__main__":
    main()