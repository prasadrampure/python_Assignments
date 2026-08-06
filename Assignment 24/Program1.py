import schedule
import psutil
import time

def ProcessInfo():
    timestamp = time.strftime("%d-%m-%Y-%H-%M-%S")
    FileName = "ProcessLog"+timestamp
    fobj = open(FileName,"a")
    fobj.write("-"*100+"\n")
    fobj.write(f"Process log file \n created at time :{time.ctime()}\n")
    fobj.write("-"*100+"\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        fobj.write("-"*100+"\n")

        fobj.write("\n")
        fobj.write(f"Process ID : {info.get("pid")}\n")
        fobj.write(f"Process Name : {info.get("name")}\n")
        fobj.write(f"Username : {info.get("username")}\n")

        fobj.write("-"*100+"\n")

    fobj.write("-"*100+"\n")
    fobj.write("-"*100+"\n")
    fobj.write("End of log file\n")
    fobj.write("-"*100+"\n")
    fobj.write("-"*100+"\n")

    print("Log file created succesfully")
    fobj.close()

def main():
    schedule.every(10).seconds.do(ProcessInfo)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()