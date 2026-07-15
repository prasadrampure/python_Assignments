import multiprocessing
import os

def Odd(n):
    print("Process Id :",os.getpid())
    if n % 2 == 0:
        count = n // 2
    else:
        count = n // 2 + 1

    print("Input number:",n)
    print("Odd number count :",count)
    print()

def main():
    Data =[1000000, 2000000, 3000000, 4000000]
    
    pobj = multiprocessing.Pool()

    pobj.map(Odd, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()