

import multiprocessing

def Prime(n):
    if n <= 1:
        return False
    
    for i in range(2,n):
        if n %2 == 0:
            return False
        
    return True

def countPrime(n):
    count = 0
    for i in range(1,n+1):
        if Prime(i):
            count += 1

    return count

    
def main():
    Data = [10000, 20000, 30000, 40000]

    Result = [] 

    pobj = multiprocessing.Pool()

    Result = pobj.map(Prime, Data)

    pobj.close()
    pobj.join()

    print("Result is :  ")
    print(Result)

if __name__ == "__main__":
    main()