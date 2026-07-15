import multiprocessing
import os

def Factorial(n):

    print("PID :",os.getpid())
    Fact = 1
    for i in range(1,n+1):
        Fact = Fact * i

    return Fact
def main():
    Data = [10,15,20,25]
    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial, Data)

    print(f"Result: {Result}")




if __name__ == "__main__":
    main()