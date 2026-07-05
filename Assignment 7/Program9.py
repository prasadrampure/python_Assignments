from functools import reduce
Product = lambda No1,No2 : No1 * No2

def main():
    No = int(input("Enter a number:"))
    S = list()
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = (reduce(Product,S))
    print("the product will be:",fRet)
    
    
if __name__ == "__main__":
    main()