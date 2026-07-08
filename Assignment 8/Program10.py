def DisplayLenght(Name):
    return len(Name)

def main():
    Name = (input("Enter a name : "))
    Ret = DisplayLenght(Name)
    print("Lenght of name :",Ret)

if __name__ == "__main__":
    main()