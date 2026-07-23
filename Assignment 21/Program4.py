import schedule
import os
import time
import datetime

def CreateLog():
    timeStamp = time.ctime()
    logFileName = "Marvellous%s.log"%(timeStamp)

    logFileName = logFileName.replace(":","_")

    fobj = open(logFileName,"w")
    print("log file gets created with name :",logFileName)

def main():

    border = "-"*40
    print(border)
    print("Marvellous log creating..")
    schedule.every(10).minutes.do(CreateLog)
    print(border)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()