import schedule
import psutil
import time
import sys 
import os

def ProcessInfo(Directoryname):

    ret = os.path.exists(Directoryname)
    if (ret == True):
        ret = os.path.isdir(Directoryname)
        if(ret == False):
            print("Print no such directory found")

    else:
        os.mkdir(Directoryname)

    timestamp = time.strftime("%d-%m-%Y-%H-%M-%S")
    FileName = os.path.join(Directoryname,f"Process_Log_File{timestamp}.log")
    fobj = open(FileName,"a")

    fobj.write("-"*100+"\n")
    fobj.write(f"Process log created at time :{time.ctime()}\n")
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
    if (len(sys.argv) == 2):
        schedule.every(10).seconds.do(ProcessInfo,sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

        else:
            print("Invalid no of arguments \n Enter correct no of arguments")

if __name__ == "__main__":
    main()