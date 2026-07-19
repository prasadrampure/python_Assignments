
def File():
    fobj1 = open("Demo.txt","r")
    fobj2 = open("ABC.txt","w")

    data = fobj1.read()

    for line in data:
        fobj2.write(line)

    print("File content get sccess")

def main():
    File()

if __name__ == "__main__":
    main()