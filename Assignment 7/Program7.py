FiveLetter = lambda No: len(No)>=5
def main():
    No = int(input("Enter a number:"))
    S = list()
    for i in range(No):
        Num = (input())
        S.append(Num)

    fRet = list(filter(FiveLetter,S))
    print("Fiveletter  are:",fRet)
    
    
if __name__ == "__main__":
    main()