Odd = lambda Num : (Num % 2 == 1)

def main():
    Num = int(input("Enter a number:"))
    Ret = Odd(Num)
    if Ret == True:
        print("Number is Odd")
    else:
        print("Number is Even")


if __name__  == '__main__':
    main()