def square(Num):
    return Num * Num
    
      

def main():
    Num = int(input("Enter the number:"))
    Ret = square(Num)
    print("Square is :",Ret)


if __name__ == "__main__":
    main()