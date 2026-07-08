def DisplayEvenNo(No):
    for i in range(2,No+1,2):
        print(i)


def main():
    No = int(input("Enter a number"))
    DisplayEvenNo(No)
    
    

if __name__ == "__main__":
    main()