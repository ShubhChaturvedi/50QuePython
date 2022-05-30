# que 38 - Write a Python program to read a random line from a file.

f = open("Miscellaneous\File handling\Que38 file1.txt" , "r")

read = f.readlines()
a = int(input("enter the line number you have to read = "))
print(read[a-1])
f.close()