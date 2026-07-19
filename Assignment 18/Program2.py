def main():
    filename = input("Enter file name :")
    count = 0

    file = open(filename,"r")
    
    for line in file:
        words = line.split()
        count = count + len(words)
    file.close()

    print("total no of words in ",count)


if __name__ == "__main__":
    main()