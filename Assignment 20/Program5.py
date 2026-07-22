import schedule
import time
import datetime

def Display():
    obj = open("Marvellous.txt","a")
    obj.write("Taask execute at :"+str(datetime.datetime.now())+"\n")

    obj.close()
    

def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()