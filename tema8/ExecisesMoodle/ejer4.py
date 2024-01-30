#4) Write two programs that compare two files (to be passed as parameter on the command line)  and determine whether these files have the same content (i.e., whether they are the same or not). Make a first version for text files and a second one for any type of file.


import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <text file1> <text file2>")
    sys.exit()

try:
    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')
except FileNotFoundError:
    print("The given files do not exist")
else:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    if len(lines1) != len(lines2):
        print("The files are different")
    else:
        i = 0
        for myline1 in lines1:
            myline2 = lines2[i]
            if myline1 != myline2:
                print("The files are different")
                break 
            i += 1
        print("The files have the same content!")
file1.close()
file2.close()

