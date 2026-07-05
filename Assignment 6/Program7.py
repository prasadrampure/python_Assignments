Divisible = lambda Num : (Num % 5 == 0)


def main():
    Num = int(input("Enter a number:"))
    Ret = Divisible(Num)
    if Ret == True:
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")

if __name__  == '__main__':
    main()