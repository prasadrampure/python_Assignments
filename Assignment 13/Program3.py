import threading
def Sum(Arr):
    Sum = 0
    for i in Arr:
        Sum += i

    print('The sum is :',Sum)

def Product(Arr):
    Product = 1
    for i in Arr:
        Product *= i

    print("Productwill be :",Product)

def main():
    No = int(input("Enter a number :"))

    Arr = []

    for i in range(No):
        Num = int(input())
        Arr.append(Num)

    T1 = threading.Thread(target = Sum,args=(Arr,))
    T2 = threading.Thread(target = Product,args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()





if __name__ == "__main__":
    main()