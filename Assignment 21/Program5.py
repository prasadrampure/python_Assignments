import schedule
import os
import time
import datetime

def Countfile(Directory_Name):

    TotalFile = 0
    for Directory,SubFolder,FileName in os.walk(Directory_Name):

        for fname in FileName:
            TotalFile += 1

        print("TotalFiles :",TotalFile)
        print("Date & Time :",datetime.datetime.now())

def main():

    border = "-"*40
    print(border)
    name = input("Enter a directory name :")

    print("Directory scanning..")

    schedule.every(1).minutes.do(Countfile,name)
   
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print(border)

if __name__ == "__main__":
    main()