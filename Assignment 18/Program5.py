def main():
    filename = input("Enter file name :")
    word = input("Enter the word:")

    file = open(filename,"r")
    
    Data = file.read()
    if word in Data:
        print("Word found")
    else:
        print("Word is not found")


if __name__ == "__main__":
    main()