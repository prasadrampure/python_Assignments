import pandas as pd
import matplotlib.pyplot as plt 

def main():
    Data = {
        "Name": ["Amit","Sagar","Pooja"],
        "Math": [85,90,78],
        "Science": [92,88,80],
        "English": [75,85,82]
    }

    df = pd.DataFrame(Data)

    print("DataFrame Created")

    print(df.describe())

    df["Total"] = df["Math"] + df["Science"] + df["English"]

    print("\n New column added to data frame")
    print(df)

    print("Student who score more than 85marks in science :")
    print(df[df["Science"] > 85])

    print("Replacing Name")

    df["Name"] = df["Name"].replace("Pooja", "Puja")
    print(df)

    print("Total Marks in Descending order")

    df = df.sort_values(by="Total", ascending=False)
    print(df)

    print("BarPolt of Total Marks Vs student name")

    plt.bar(df["Name"], df["Total"])

    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("BarPolt of Total Marks Vs Student Name")

    plt.show()

    print("Line chart of Marks for Amit Across All subject")
    Amit = df[df["Name"] == "Amit"].iloc[0]

    Subjects = ["Math", "Science", "English"]

    Marks = [Amit["Math"], Amit["Science"], Amit["English"]]

    plt.plot(Subjects,Marks, marker="o")

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amits Marks Across All Subjects")

    plt.show()

if __name__ == "__main__":
    main()