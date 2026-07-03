def Area(Radius):
    Area = 3.14 * Radius * Radius
    return Area
    


def main():
    Radius = int(input("Enter the radius:"))
    Ret = Area(Radius)
    print("Area of circle is:",Ret)
    
if __name__ == "__main__":
    main()