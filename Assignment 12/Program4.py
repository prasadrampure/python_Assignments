import threading
def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1

    print("Thread Id :", threading.get_ident())
    print("Thread name :",threading.current_thread().name)
    print("Lower letters :",count)
    print()

def Capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1

    print("Thread Id :", threading.get_ident())
    print("Thread name :",threading.current_thread().name)
    print("Capital letters :",count)
    print()

def Digit(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1

    print("Thread Id :", threading.get_ident())
    print("Thread name :",threading.current_thread().name)
    print("Digits :",count)
    print()
    

def main():
    s = input("Enter a string :")

    T1  = threading.Thread(target = Small, args = (s,), name="Small")
    T2  = threading.Thread(target = Capital, args = (s,), name="Capital")
    T3  = threading.Thread(target = Digit, args = (s,), name="Digit")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()