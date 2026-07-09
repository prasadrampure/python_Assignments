import threading

def Even(Arr):
    for i in range(len(Arr)):
            if(Arr[i] % 2 == 0):
                    print("Even no are :",Arr[i])

            print()

def Odd(Arr):
    for i in range(len(Arr)):
            if(Arr[i] % 2 != 0):
                 print("Odd no are :",Arr[i])

            print()

    
def main():

    No = int(input("Enter a number :"))
    Arr = []
    print("Enter the elements")
    for i in range(No):
            Num = int(input())
            Arr.append(Num)

    T1 = threading.Thread(target = Even,args=(Arr,))
    T2 = threading.Thread(target = Odd,args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
         