def ChkGreater(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2



def main():
    No1 = int(input("Enter First Number:"))
    No2 = int(input("Enter Second Number:"))
    ChkGreater(No1,No2)
    Ret = ChkGreater(No1,No2)
    if Ret == True :
        print(No1, "Is Grater")
    else:
        print(No2, "Is grater")



if __name__ == "__main__":
    main()