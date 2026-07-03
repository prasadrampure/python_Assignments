def Area(No1,No2):
    Area = No1 * No2
    return Area


def main():
    No1 = int(input("Enter the length:"))
    No2 = int(input("Enter the weidth:"))

    Ret = Area(No1,No2)
    print("Area is:",Ret)


if __name__ == "__main__":
    main()