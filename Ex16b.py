from sys import argv

script, file1, file2 = argv

A = open(file1,'r')
print A.read()
A.close()
B = open(file1,'w')
B.truncate()
B.write("\n")
B.write("Youppi!")
B.close()
A = open(file1,'r')
print A.read()
