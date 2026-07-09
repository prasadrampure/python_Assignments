import CalculatePrime

def ListPrime(Data):
    sum = 0

    for No in Data:
        if CalculatePrime.ChkPrime(No):
            sum = sum + No

    return sum

def main():
    size = int(input("Enter no of elements :"))

    Arr = []

    print("Enter the elements :")
    for i in range(size):
        value = int(input())
        Arr.append(value)
  
    Result = ListPrime(Arr)
    print("Addition of no is :",Result)

if __name__ == "__main__":
    main()