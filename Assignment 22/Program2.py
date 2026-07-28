import os 
import datetime
import time

def MonitorFile(filename):
    while True:
        size = os.path.getsize(filename)

        with open("FileSizeLog.txt","a") as f:
            f.write(f"File Name : {filename}\n")
            f.write(f"File Size : {size} bytes\n")
            f.write(f"Date & Time : {datetime.datetime.now()}\n")
            f.write("-"*40 + "\n")

        print("File size loged successfully")
        time.sleep(30)

def main():
    name = input("Enter file name :")
    MonitorFile(name)

if __name__ == "__main__":
    main()