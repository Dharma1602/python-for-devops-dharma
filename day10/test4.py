import os
folders = input("please provide list of folder names with spaces in between: " ).split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like the folder does not exist:" + folder)
        #break (this is to break the for loop after an error)
        #continue (to continue the for loop after an error)
        continue
    except PermissionError:
        continue
        print("No access to this folder:" + folder)

    print("====listing files for the folder - " + folder)
    #print(files)
    for file in files:
        print(file)