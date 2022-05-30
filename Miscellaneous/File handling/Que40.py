# que 40 - Write a Python program to copy the contents of a file to another file .


f = open("Que40 file1.txt" , "r")
read = f.read()
g = open("Que40 file2.txt" , "w")
write = g.write(read)
f.close()
g.close()