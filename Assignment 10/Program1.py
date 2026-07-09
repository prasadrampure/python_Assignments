def CalculateSum(S):
    Sum = 0
    for i in range(len(S)):
        Sum += S[i]

    return Sum

def main():
    No = int(input("Enter a number :"))

    S = []

    for i in range(No):
        Num = int(input())
        S.append(Num)

    Ret = CalculateSum(S)
    print("Sum is :",Ret)

if __name__ == "__main__":
    main()