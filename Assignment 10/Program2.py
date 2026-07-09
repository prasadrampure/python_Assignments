def Max(S):
    Max = S[0]
    for i in range(len(S)):
        if (S[i] > Max):
            Max = S[i]
    
    return Max

def main():
    No = int(input("Enter a number :"))

    S = []

    for i in range(No):
        Num = int(input())
        S.append(Num)

    Ret = Max(S)
    print("Maximum no  :",Ret)

if __name__ == "__main__":
    main()