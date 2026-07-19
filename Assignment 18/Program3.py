def main():
    filename = input("Enter file name :")
    
    file = open(filename,"r")
    
    for line in file:
        print(line)
        
    file.close()

   


if __name__ == "__main__":
    main()