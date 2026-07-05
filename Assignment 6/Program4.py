Min = lambda No1,No2 : No1 < No2
def main():
    No1 = int(input("enter first number:"))
    No2 = int(input('enter second number:'))
    Ret = Min(No1,No2)
    if Ret == True:
        Ret = No1
    else:
        Ret = No2
    print("Minimum Num is:",Ret)

if __name__ == "__main__":
    main()