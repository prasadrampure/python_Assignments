Divisible = lambda No : (No%3==0)and(No%5==0)

def main():
    No = int(input("Enter a number:"))
    S = list()
    for i in range(No):
        Num = int(input())
        S.append(Num)

    fRet = list(filter(Divisible,S))
    print("No is Divisible by 3&5:",fRet)
    
    
if __name__ == "__main__":
    main()