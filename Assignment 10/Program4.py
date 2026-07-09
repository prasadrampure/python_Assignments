def Frequency(S,Value):
    count = 0
    for i in range(len(S)):
        if (S[i] == Value):
            count = count + 1

    return count
def main():
    No = int(input("Enter a number :"))

    S = []

    for i in range(No):
        Num = int(input())
        S.append(Num)

    Value = int(input('Calculated frequency :'))

    Ret = Frequency(S,Value)
    print("Frequency is :",Ret)

    

if __name__ == "__main__":
    main()