import sys
print("configuration A")
file = open(sys.argv[0], "r")
lines = file.readlines()
file.close()
if(lines[1][21] == "A"):
	lines[1] = 'print("configuration B")\n'
else:
	lines[1] = 'print("configuration A")\n'
file = open(sys.argv[0], "w")
for line in lines:
	file.write(line)