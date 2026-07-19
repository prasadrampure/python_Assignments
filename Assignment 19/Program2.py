def Content(name):
    fobj = open(name,"r")

    Data = fobj.read()
    print(Data)

def main():
    name = input("Enter file name ")

    Content(name)
   

    
if __name__ == "__main__":
    main()