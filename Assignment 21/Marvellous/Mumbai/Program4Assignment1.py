def Cube(Num):
    return Num * Num * Num


def main():
    Num = int(input("Enter First Number:"))
    Ret = Cube(Num)
    print("Cube is :",Ret)

if __name__ == "__main__":
    main()