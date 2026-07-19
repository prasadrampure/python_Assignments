def Frequency(name,string):
    count = 0
    fobj = open(name,"r")

    data = fobj.read()

    for word in data.split():
        if word == string:
            count = count+1
    return count

def main():
    name = input("Enter file name")
    string = input("Enter the string")

    Ret = Frequency(name,string)
    print("Frequency is :",Ret)


if __name__ == "__main__":
    main()