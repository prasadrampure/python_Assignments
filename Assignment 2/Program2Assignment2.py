def SumNatural(Num):

    sum = 0
    for i in range(0,Num+1):
        sum = sum + i
    return sum


def main():

    Num = int(input("Enter a number:"))
    Ret = SumNatural(Num)
    print("The Sum of natural no is :",Ret)

if __name__ == "__main__":
    main()