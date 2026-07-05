from functools import reduce

Addition = lambda No1, No2: No1 + No2

def main():
    No = int(input("Enter a number:"))
    S = []
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = (reduce(Addition,S))
    print("Addition are:",fRet)
    
if __name__ == "__main__":
    main()