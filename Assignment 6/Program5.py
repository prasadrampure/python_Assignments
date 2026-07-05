Even = lambda Num : (Num % 2 == 0)

def main():
    Num = int(input("Enter a number:"))
    Ret = Even(Num)
    if Ret == True:
        Ret = "True"
        print("Number is Even")
    else:
        Ret = "False"
        print("Number is odd")


if __name__ == "__main__":
    main()