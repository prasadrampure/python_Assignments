import threading

def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def prime(S):

    print("Prime numbers:")
    for i in S:
        if CheckPrime(i):
            print(i,end = "")
        print()

def Nonprime(S):
    print("Non prime numbers:")
    for i in S:
            if not CheckPrime(i):
                    print(i, end="")

            print()

def main():
    No = int(input("Enter a number :"))

    S = []

    for i in range(No):
        Num = int(input())
        S.append(Num)

    T1 = threading.Thread(target = prime,args=(S,))
    T2 = threading.Thread(target = Nonprime,args=(S,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()





if __name__ == "__main__":
    main()