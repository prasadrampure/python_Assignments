

import multiprocessing
import time


def Nnumber(n):
    total = 0
    for i in range(1,n+1):
        total = total + (i**5)

    print("Input number :",n)
    print("Sun :",total)

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    pobj.map(Nnumber, Data)

    pobj.close()
    pobj.join()
    end_time = time.perf_counter()

    
    print(f"Time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()