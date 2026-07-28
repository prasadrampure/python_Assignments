import schedule
import datetime
import time

def CreateFile():
    timeStamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    FileName = f"File{timeStamp}.txt"

    fobj = open(FileName,"w")
    print("Date & Time :",datetime.datetime.now())

    fobj.close()
  
def main():
    print("File gets creating..")

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    