from functools import reduce

def Check(no):
    return no % 2 == 0

def Square(no):
    return no * no

def Add(x,y):
    return x + y

def main():
    size = int(input("Enter no of elements :"))

    Data = []

    print("enter a elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("input list :",Data)

    fData = list(filter(Check, Data))
    print("Filtered Data :",fData)

    mData = list(map(Square, fData))
    print("Squared Data :",mData)

    result = reduce(Add, mData)
    print("Product is :",result)


if __name__ == "__main__":
    main()