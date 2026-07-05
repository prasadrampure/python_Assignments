Cube = lambda Num : (Num * Num * Num)

def main():
    Num = int(input("Enter a number:"))
    Ret = Cube(Num)
    print('Cube is :',Ret)

if __name__ == "__main__":
    main()