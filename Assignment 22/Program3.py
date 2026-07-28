import schedule
import os
import time

def DisplayFileContent(Filepath):
    if(os.path.exists(Filepath) == False):
        return FileNotFoundError
    elif(os.path.getsize(Filepath) == 0):
        return FileExistsError
    elif(os.access(Filepath,os.R_OK) == False):
        return PermissionError
    else:      
        fobj = open(Filepath,"r")
        ret = fobj.read()
        print(ret)

def main():
    Filepath = input("Enter the filename or path :")

    schedule.every(10).seconds.do(DisplayFileContent,Filepath)

    while True:
        schedule.run_pending()
        time.sleep(1)
     
if __name__ == "__main__":
    main()