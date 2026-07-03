def Divisible(Num):

    if Num % 3 == 0 and Num % 5 == 0:
        return True
    else:
        return False


def main():
    Num = int(input('Enter the number :'))
    Ret = Divisible(Num)
    if Ret == True:

        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
     

if __name__ == "__main__":
    main()
