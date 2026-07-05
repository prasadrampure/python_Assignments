from functools import reduce
Maximum = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = (reduce(Maximum,S))
    print("Maximum no is:",fRet)
    
if __name__ == "__main__":
    main()