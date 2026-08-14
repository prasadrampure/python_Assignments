import math

def KNNClassifier():
    border = "-"*40

    print(border)
    print("Student Pass/Fail Prediction")
    print(border)

    Data = [
        {"StudyHours" : 2, "Attendance" : 60, "Result" : "Fail"},
        {"StudyHours" : 5, "Attendance" : 80, "Result" : "Pass"},
        {"StudyHours" : 6, "Attendance" : 85, "Result" : "Pass"},
        {"StudyHours" : 1, "Attendance" : 50, "Result" : "Fail"}
    ]

    StudyHours = int(input("Enter Study Hours :"))
    Attendance = int(input("Enter Attendance :"))

    Distances = []

    for point in Data:
        Distance = math.sqrt(
            (StudyHours - point["StudyHours"])**2 +
            (Attendance - point["Attendance"])**2
        )

        Distances.append({
            "Distance" : Distance,
            "Result" : point["Result"]
        })

    Distances.sort(key=lambda x: x["Distance"])

    k = 3
    Neighbours = Distances[:k]

    PassCount = 0
    FailCount = 0

    for neighbor in Neighbours:
        if neighbor["Result"] == "Pass":
            PassCount += 1
        else:
            FailCount += 1

    if PassCount > FailCount:
        Prediction = "Pass"
    else:
        Prediction = "Fail"

    print(border)
    print("Predicted Result :",Prediction)
    print(border)

def main():
    KNNClassifier()

if __name__ == "__main__":
    main()