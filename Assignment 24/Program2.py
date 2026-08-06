import schedule
import psutil
import time
import sys 

def ProcessInfo(Processname):

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid","name","username","status"])
        pname = info.get("name")

        if(Processname == pname):

            print(f"Process Id : {info.get("pid")}")
            print(f"Process name : {info.get("name")}")
            print(f"Username : {info.get("username")}")
            print(f"Status of process : {info.get("status")}")
            return
        
        print("Process not found : check processname again")
        
def main():
    if (len(sys.argv) == 2):
        schedule.every(10).seconds.do(ProcessInfo,sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

        else:
            print("Invalid no of arguments \n Enter correct no of arguments")

if __name__ == "__main__":
    main()