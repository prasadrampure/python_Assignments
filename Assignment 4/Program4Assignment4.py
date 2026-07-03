def Display(No):

    for i in range(1, No+1):
        print(i)

def main():
    No = int(input("Enter a number:"))
    
    Display(No)

if __name__ == "__main__":
    main()