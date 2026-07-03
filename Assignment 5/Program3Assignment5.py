def Perfect(No):
    Sum = 0
    for i in range(1, No):
        if(No%i == 0):
            Sum = Sum + i
    if Sum == No:
        return True
    else:
        return False

def main():
    No = int(input('Enter a number:'))
    Ret = Perfect(No)
    if (Ret):
        print("Number is perfect")
    else:
        print("Number is not perfect")

if __name__ == "__main__":
    main()