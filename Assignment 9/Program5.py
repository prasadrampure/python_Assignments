def Prime(No):
    if No<=1:
        return False
    for i in range(2,No):
        if (No % 2 == 0):
            return True
        else:
            return False
    

def main():
    No = int(input("Enter a number :"))
    Ret= Prime(No)
    if (Ret):
        print("Number is prime")
    else:
        print("Number is not prime")
   

if __name__ == "__main__":
    main()
