import sys

type = sys.argv[1]

if type == "t2.Micro":
    print("THis will cost 2 dollars")
elif type == "t2.Medium":
    print("This will cost 4 dollars")
elif type == "t2.Xlarge":
    print("This will cost 8 dollars")
else:
    print("please check the input type")