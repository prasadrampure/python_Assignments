
def CompareFile():
    filename1 = input("Enter file name:")
    fobj1 = open(filename1,"r")

    filename2 = input("Enter file name:")
    fobj2 = open(filename2,"r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    if(Data1 == Data2):
        print("Success")

    else:
        print("Faliur")

def main():
    CompareFile()

if __name__ == "__main__":
    main()