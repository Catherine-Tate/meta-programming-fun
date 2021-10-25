import sys
print("configuration A")
file = open(sys.argv[0], "r")
lines = file.readlines()
file.close()
file = open("newFile.py", "x")
for line in lines:
	file.write(line)