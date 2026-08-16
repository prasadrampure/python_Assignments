import pandas as pd

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

if __name__ == "__main__":
    main()