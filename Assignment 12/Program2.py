import threading

def EvenFactor(No):
    for i in range(No):
        if No %2 == 0:
            print("Even Factors :",i)

        print()

def OddFactor(No):
    for i in range(No):
        if No % 2 != 0:
            print("Odd Factors :",i)

        print()

    
def main():

    No = int(input("Enter a number :"))
    

    T1 = threading.Thread(target = EvenFactor,args=(No,))
    T2 = threading.Thread(target = OddFactor,args=(No,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
         