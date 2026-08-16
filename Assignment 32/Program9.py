import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    border = "-"*50
    Data = {
            "Name": ["Amit","Sagar","Pooja"],
            "Gender": ["Male", "Male", "Female"],
            "Math": [85,90,78],
            "Science": [92,88,80],
            "English": [75,85,82]
        }
    
    df = pd.DataFrame(Data)

    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

    print(border)
    print("Min-Max Scaling")
    print(border)   

    scaler = MinMaxScaler()

    df["Math"] = scaler.fit_transform(df[["Math"]])
    print(df)

    print(border)
    print("One-Hot Encoding")
    print(border)

    df = pd.get_dummies(df, columns=["Gender"], dtype=int)
    print(df)

    print(border)
    print("Average Marks By Gender")
    print(border)

    df["Average"] = df[["Math","Science","English"]].mean(axis=1)

    result = df.groupby(["Gender_Female","Gender_Male"])["Average"].mean()

    print(result)

    print(border)
    print("Pie chart of Sagar Marks")
    print(border)

    Sagar = df[df["Name"] == "Sagar"].iloc[0]

    Subjects = ["Math","Science","English"]
    Marks = [Sagar["Math"], Sagar["Science"], Sagar["English"]]

    plt.pie(Marks, labels=Subjects, autopct="%1.1f%%")
    plt.title("Sagar Subjects Marks")
    plt.show()

    print(border)
    print("Status Column")
    print(border)

    df["Status"] = np.where(df["Total"] >= 250, "Pass", "Fail")

    print(df)

    print(border)
    print("Count Pass")
    print(border)

    PassCount = (df["Status"] == "Pass").sum()

    print("No of Students Passed :",PassCount)

    print(border)
    print("Csv file Export")
    print(border)

    df.to_csv("Students_final.csv", index=False)

    print("Final DataFrame Exported to Students_final.csv")

    print(border)
    print("Histogram of Math Marks")
    print(border)

    plt.hist(df["Math"], bins=5)

    plt.xlabel("Marks")
    plt.ylabel("Students")
    plt.title("Histogram of Math Marks")

    plt.show()
    
if __name__ == "__main__":
    main()