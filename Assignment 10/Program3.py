def Min(S):
    Min = S[0]
    for i in range(len(S)):
        if (S[i] < Min):
            Min = S[i]
    
    return Min

def main():
    No = int(input("Enter a number :"))

    S = []

    for i in range(No):
        Num = int(input())
        S.append(Num)

    Ret = Min(S)
    print("Minimum  no  :",Ret)

if __name__ == "__main__":
    main()