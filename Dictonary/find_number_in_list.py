x = int(input("Enter the no. of elements:"))
a=[]
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)
z = int(input("Enter the no.want to find:"))
b = 0
for i in range(x):
    if(a[i]==z):
        b = 1
        pos = i + 1
        break
if(b==1):
    print("Yes! at",pos,"position" )
else:
    print("No!")
