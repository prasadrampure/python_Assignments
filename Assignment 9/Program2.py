def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end="")
        print()

def main():
    No = int(input("Enter a number :"))
    DisplayPattern(No)

if __name__ == "__main__":
    main()
