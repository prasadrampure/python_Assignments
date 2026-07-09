from functools import reduce

def Prime(no):
    if no <= 1:
        return False
    
    for i in range(2, no):
        if no % 2 == 0:
            return False
        
    return True
    

def Multiply(no):
    return no * no

def Maximum(x,y):
    if x > y:
        return x
    else:
        return y

def main():
    size = int(input("Enter no of elements :"))

    Data = []

    print("enter a elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("input list :",Data)

    fData = list(filter(Prime, Data))
    print("Filtered Data :",fData)

    mData = list(map(Multiply, fData))
    print("Multiplied Data :",mData)

    result = reduce(Maximum, mData)
    print("Maximum no is :",result)


if __name__ == "__main__":
    main()