import os

def main():
    filename = input("Enter file name ")
    file = open(filename,"r")

    File = os.path.exists(filename)
    if(File == True):
        print("file is present")
    else:
        print("file is not present")


if __name__ == "__main__":
    main()