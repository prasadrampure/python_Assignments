import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix
)

Border = "-"*30

print(Border)
print("First Five & Last five Dataset loaded Succesfully")
print(Border)

StudentData = "student_performance_ml.csv"

sd = pd.read_csv(StudentData)

print(sd.head())
print(sd.tail())

print(Border)
print("Total Number of Rows and Columns")
print(Border)

print("Total Rows :",sd.shape[0])
print("Total Columns :",sd.shape[1])

print(Border)
print("Column Names")
print(Border)

print(list(sd.columns))

print(Border)
print("Datatype of each columns")
print(Border)

print(sd.dtypes)

print(Border)
print("Total No of students")
print(Border)

print(sd.shape[0])

print(Border)
print("total no of students passed")
print(Border)

print(sd["FinalResult"].value_counts()[1])

print(Border)
print("total no of students failed")
print(Border)

print(sd["FinalResult"].value_counts()[0])

print(Border)
print("Calculation of student dataset")
print(Border)

print("Average StudyHoures :",sd["StudyHours"].mean())
print("Average Attendance :",sd["Attendance"].mean())
print("Maximum previous score :",sd["PreviousScore"].max())
print("/minimum sleep hours :",sd["SleepHours"].min())

print(Border)
print("Calculate Percentage of Pass & Fail")
print(Border)

result_count = sd["FinalResult"].value_counts()

Pass_count = result_count[1]
Fail_count = result_count[0]

Total = len(sd)

Pass_percentage = (Pass_count / Total) * 100
Fail_percentage = (Fail_count / Total) * 100 

print("Pass Students :",Pass_count)
print("Fail Students :",Fail_count)
print("Pass Percentage :",Pass_percentage)
print("Fail Percentage :",Fail_percentage)

print(Border)
print("Average of studyhours & Attendance by Final Result")
print(Border)

print("Average StudyHours :")
print(sd.groupby("FinalResult")["StudyHours"].mean())

print()

print("Average Attendance :")
print(sd.groupby("FinalResult")["Attendance"].mean())  

print(Border)
print("Train the model")
print(Border)

X = sd[["StudyHours",
       "Attendance",
       "PreviousScore",
       "AssignmentsCompleted",
       "SleepHours"]]

Y = sd["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5, random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train, Y_train)

print("Model train succesfully")

print(Border)
print("Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Predicted values :")
print(Y_pred)

print("\nActual values :")
print(Y_test.values)

print(Border)
print("Accuracy of model")
print(Border)

Accuracy = accuracy_score(Y_pred,Y_test)

print(f"Accuracy : {Accuracy * 100:.2f}%")

print(Border)
print("Confusion matrix")
print(Border)

cm = confusion_matrix(Y_pred,Y_test)
print(cm)

print(Border)
print("Acuracy of Training & testing")
print(Border)

Y_train_pred = model.predict(X_train)

Y_test_pred = model.predict(X_test)

Train_Accuracy = accuracy_score(Y_train, Y_train_pred)
Test_Accuracy = accuracy_score(Y_test, Y_test_pred)

print(f"Traning Accuracy : {Train_Accuracy * 100:.2f}%")
print(f"Testing Accuracy : {Test_Accuracy * 100:.2f}%")

print(Border)
print("Maximum Depth")
print(Border)

model1 = DecisionTreeClassifier(max_depth=1,random_state=42)
model1.fit(X_train,Y_train)

Y_pred1 = model1.predict(X_test)
Accuracy1 = accuracy_score(Y_test,Y_pred1)

model3 = DecisionTreeClassifier(max_depth=3,random_state=42)
model3.fit(X_train,Y_train)

Y_pred3 = model3.predict(X_test)
Accuracy3 = accuracy_score(Y_test,Y_pred3)

model_None = DecisionTreeClassifier(max_depth=None,random_state=42)
model_None.fit(X_train,Y_train)

Y_pred_none = model_None.predict(X_test)
Accuracy_None = accuracy_score(Y_test,Y_pred_none)

print("Testing Accuracy")
print(Border)
print("Max Depth 1 :",Accuracy1)
print("Max Depth 3 :",Accuracy3)
print("Max Depth None :",Accuracy_None)

print(Border)
print("Predict student result")
print(Border)

Student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

Prediction = model.predict(Student)

print("Predicted result :",Prediction[0])

if Prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
