import threading
def Max(Arr):

    Max = Arr[0]
    for i in range(len(Arr)):
        if (Arr[i] > Max):
            Max = Arr[i]

    print("Miximum no are :",Max)


def Min(Arr):

    Min = Arr[0]
    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    print("Minimum no are:",Min)



def main():
    No = int(input("Enter a number :"))

    Arr = []

    for i in range(No):
        Num = int(input())
        Arr.append(Num)

    T1 = threading.Thread(target = Max,args=(Arr,))
    T2 = threading.Thread(target = Min,args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()





if __name__ == "__main__":
    main()