import schedule
import os
import time
import shutil

def CopyTxtFile(SrcDirectorypath,DestDirectorypath):
    if(os.path.isdir(SrcDirectorypath) == False):
        return NotADirectoryError("Source directory not present.")
    if(os.path.isdir(DestDirectorypath) == False):
        return NotADirectoryError("Destination Directory not present.")
    
    fobj = open("FileCopyLog","a")

    for folder,subfolder,files in os.walk(SrcDirectorypath):
        for fname in files:
            SrcFileName = os.path.join(folder,fname)
            if(SrcFileName.endswith(".txt")):
                shutil.copy(SrcFileName,DestDirectorypath)
                fobj.write("\n")
                fobj.write("File Log:")
                fobj.write("\n")
                fobj.write("-"*50)
                fobj.write("\n")
                fobj.write("Files Coppied :\n")
                fobj.write("\n") 
                fobj.write(fname)
                fobj.write("\n")
                

    print("File copy succesfully")
    
def main():
    SrcDirectorypath = input("Enter Source Directory name or path :")
    DestDirectorypath = input("Enter Destination Directory name or path :")

    schedule.every(10).seconds.do(CopyTxtFile,SrcDirectorypath,DestDirectorypath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()