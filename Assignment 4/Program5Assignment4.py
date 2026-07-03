def DisplayReverse(No):

    while No > 0:
        print(No)
        No = No - 1
        

def main():
    No = int(input("Enter a number:"))
    
    DisplayReverse(No)

if __name__ == "__main__":
    main()