f = open("Que35file1.txt" , "r")

read = f.read().split()
max = "a"
for i in read:
    if len(max)<len(i):
        max = i
print(max)  
lst = []
for i in read:
    if len(i)==len(max):
        lst.append(i)

print(lst)


# longest line
wr = "a"
line = f.readlines()
print(line)
for i in line:
    if len(wr)<len(i):
        wr = i
print(wr)
f.close() 