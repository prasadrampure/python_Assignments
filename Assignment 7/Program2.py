EvenNum = lambda No: No % 2 == 0

def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = list(filter(EvenNum,S))
    print("Even numbers are:",fRet)
    
if __name__ == "__main__":
    main()