Square = lambda No: No * No


def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    Ret = list(map(Square,S))
    print("Square are:",Ret)


if __name__ == "__main__":
    main()