from functools import reduce

def Check(no):
    return no >= 70 and no <= 90

def Increase(no):
    return no + 10

def Product(x,y):
    return x * y

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

    mData = list(map(Increase, fData))
    print("Increase Data ;",mData)

    result = reduce(Product, mData)
    print("Product is :",result)


if __name__ == "__main__":
    main()