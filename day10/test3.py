import os
folders = input("please provide list of folder names with spaces in between: " ).split()
for folder in folders:
    files = os.listdir(folder)
    print("====listing files for the folder - " + folder)
    #print(files)
    for file in files:
        print(file)
