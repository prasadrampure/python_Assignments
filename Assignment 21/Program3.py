import os
import datetime

def ScanDirectory():
    path = input("Enter directory path :")

    file_count = 0
    folder_count = 0
    
    for FolderName,SubFolder,FileName in os.walk(path):
        print("Directory scanned:",FolderName)
        file_count += len(FileName)
        folder_count += len(SubFolder)

    print("Total files :",file_count)
    print("Total Subdirectories :",folder_count)
    print("Scan time :",datetime.datetime.now())

def main():
    ScanDirectory()
    
if __name__ == "__main__":
    main() 