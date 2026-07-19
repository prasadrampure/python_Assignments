def main():
    filename = input("Enter file name :")
    count = 0

    file = open(filename,"r")
    
    for line in file:
        count = count + 1
    file.close()

    print("total no of lines in ",count)


if __name__ == "__main__":
    main()