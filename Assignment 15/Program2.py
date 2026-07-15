import multiprocessing
import os
import time
def SumOdd(No):
    print("PID :",os.getpid())
    Sum = 0
    for i in range(1,No+1):
        if i % 2 == 1:
            Sum = Sum + i

    return Sum


def main():
    Data =[1000000, 2000000, 3000000, 4000000]
    Result= []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    end_time = time.perf_counter()
    print(f"Result: {Result}")
    print(f"Time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()