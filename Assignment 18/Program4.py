def main():
    filename1 = input("Enter file name :")
    filename2 = input("Enter new file name:")
    file1 = open(filename1,"r")
    file2 = open(filename2,"w")
    
    for line in file1:
        file2.write(line)
        
    file1.close()
    file2.close()

    print("Cntents of", filename1, "copied into", "filename2")

   
if __name__ == "__main__":
    main()