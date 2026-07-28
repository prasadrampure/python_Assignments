import schedule
import time
import os
import shutil

def CleanDirectory(Directorypath):
    if(os.path.isdir(Directorypath) == False):
        return NotADirectoryError("Directory not present.")

    fobj = open("DirectoryCleanLog","a")
    fobj.write("-"*50)
    fobj.write("\n")
    fobj.write("File Log:")
    fobj.write("\n")
    fobj.write("-"*50)
    fobj.write("\n")
    fobj.write("Files Deleted :\n")

    for folder,subfolder,files in os.walk(Directorypath):
        for fname in files:
            SrcFileName = os.path.join(folder,fname)
            if(os.access(SrcFileName,os.R_OK) == True):
                if(os.path.getsize(SrcFileName) == 0):
                    fobj.write("\n")
                    fobj.write(SrcFileName)
                    fobj.write("\n")
                    os.remove(SrcFileName)
                else:
                    return PermissionError("File Cannot be read",SrcFileName)
    
    print("Files deleted succesfully")


def main():
    Directorypath = input("Enter directory name :")

    schedule.every(10).seconds.do(CleanDirectory,Directorypath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()