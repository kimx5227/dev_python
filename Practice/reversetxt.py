myfile = open("test.txt", "r")
newfile = open("reversedtest.txt", "w")
linesoffiles = myfile.readlines()
for lines in linesoffiles[::-1]:
    newfile.write(lines)
myfile.close()
