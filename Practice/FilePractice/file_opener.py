# File Objects

# two ways to open files:
# 1: assign open("file_name") to var and close it when done
# 2:use content manager to operate

# 1st method
f = open(r"D:\dev\Practice\FilePractice\sample.txt")
print(f.mode)
f.close()

# 2nd method, all operations such as reading and writing must be done in block
with open(r"D:\dev\Practice\FilePractice\sample.txt") as f:
    #print("This reads in each line of file and prints it out")
    # for line in f:
    #    print(line, end='')
    #print("\n", "Printing out first 5 lines")
    # f_contents = f.read(100) #prints first 100 characters of file
    #print(f_contents, end='')
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
print(f.mode)  # mode is still available as variable outside block, but cannot be worked on
