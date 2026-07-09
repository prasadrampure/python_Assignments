import threading

def EvenList(S):
    for i in S:
        if(i % 2 == 0):
            print("Even List :",i)
    

def OddList(S):
    for i in S:
        if(i % 2 != 0):
            print("Odd List :",i)
    
    
def main():

    No = int(input("Enter a number :"))
    
    S = []
    print("List :")
    for i in range(No):
        Num = int(input())
        S.append(Num)



    T1 = threading.Thread(target = EvenList,args=(S,))
    T2 = threading.Thread(target = OddList,args=(S,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
         