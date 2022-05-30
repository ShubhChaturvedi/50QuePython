# que 37 - Write a Python program to remove newline characters from a file.

f = open("Miscellaneous\File handling\Que36 file1.txt" , "r")
g = open("Miscellaneous\File handling\Que36 file2.txt" , "a")
read = f.readlines()
for item in read:
    item2 = item.strip()
    write = g.write(item2)

f.close()
g.close()