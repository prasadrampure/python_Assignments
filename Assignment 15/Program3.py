import multiprocessing
import os

def Even(n):
    print("Process Id :",os.getpid())
    count = n // 2
    print("Input number:",n)
    print("Even number count :",count)
    print()

def main():
    Data =[1000000, 2000000, 3000000, 4000000]
    
    pobj = multiprocessing.Pool()

    pobj.map(Even, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()