import threading

def Thread1():
    print("Thread1:")
    for i in range(1,51):
        print(i, end="")
    print()

def Thread2():
    print("Thread2:")
    for i in range(50,0,-1):
        print(i, end="")
    print()

def main():
    T1 = threading.Thread(target = Thread1, name = "Thread1")
    T2 = threading.Thread(target = Thread2, name = "Thread2")

    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()