OddNum = lambda No: No % 2 == 1

def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = list(filter(OddNum,S))
    print("Odd numbers are:",fRet)
    
if __name__ == "__main__":
    main()