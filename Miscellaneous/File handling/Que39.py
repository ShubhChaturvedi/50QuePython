# que 39 - Write a Python program to combine each line from first file with the corresponding line in second file.

f = open("Miscellaneous\File handling\Que39 file1.txt" , "r")
g = open("Miscellaneous\File handling\Que39 file2.txt" , "r")
read = f.readlines()
read2 = g.readlines()
h =open("Miscellaneous\File handling\Que39 file3.txt", "a")
a = len(read) if len(read)<len(read2) else len(read2)
for i in range(a):
    b = h.write(read[i]+read2[i])
print("finish")
f.close()
g.close()
h.close()


