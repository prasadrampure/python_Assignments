from functools import reduce
Minimum = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = (reduce(Minimum,S))
    print("Minimum no is:",fRet)
    
    
if __name__ == "__main__":
    main()