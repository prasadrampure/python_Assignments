import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def StudentData(DataPath):
  
  Border = "-"*30
  
  print(Border)
  print("First Five & Last five Dataset loaded Succesfully")
  print(Border)
  
  sd = pd.read_csv(DataPath)
  
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
  print("Histogram of StudyHours")
  print(Border)
  
  plt.figure(figsize=(7,5))
  plt.hist(sd["StudyHours"],bins = 10)
  
  plt.title("Histogram of StudyHours")
  plt.xlabel("Study Hours")
  plt.ylabel("No of students")
  
  plt.show()
  print("The histogram shows the bar graph of Students studing fo hours \n The higher graph shows that the most students studies for log time consistently \n and few students does not study-hour. \n this shows the diffrence thrugh histogram.")
  
  print(Border)
  print("Scatter plot studyhours vs previousScore")
  print(Border)
  
  plt.figure(figsize=(7,5))
  plt.scatter(sd["StudyHours"], sd["PreviousScore"])
  
  plt.title("Scatter plot")
  plt.xlabel("Study Hours")
  plt.ylabel("PerviousScore")
  
  plt.show()
  
  print(Border)
  print("Boxplot for attendance")
  print(Border)
  
  plt.figure(figsize=(7,5))
  plt.boxplot(sd["Attendance"])
  
  plt.title("Box Plot")
  plt.ylabel("Attendance")
  
  plt.show()
  
  print(Border)
  print("Observation of AssignmentCompleted & FinalResult")
  print(Border)
  
  plt.figure(figsize=(7,5))
  sd.boxplot(column = "AssignmentsCompleted", by = "FinalResult")
  
  plt.title("Observation of AssignmentCompleted & FinalResult")
  plt.xlabel("Final Result")
  plt.ylabel("AssignmentCompleted")
  
  plt.show()
  
  print(Border)
  print("Observation of SleepHours Against FinalResult")
  print(Border)
  
  plt.figure(figsize=(7,5))
  sd.boxplot(column = "SleepHours", by = "FinalResult")
  
  plt.title("Observation of SleepHours against FinalResult")
  plt.xlabel("Final Result")
  plt.ylabel("SleepHours")
  
  plt.show()

def main():
  StudentData("student_performance_ml.csv")
  
if __name__ == "__main__":
  main(
