def Display(Marks):
    if Marks >=75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    elif Marks < 50:
        print("Fail") 

def main():
    Marks = int(input("enter a Marks:"))
    Display(Marks)

if __name__ == "__main__":
    main()