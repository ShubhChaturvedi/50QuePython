a=int(input('Enter a 10 digit number :'))
count=1
e_sum=0
o_sum=0
while(a>0):
    if(count%2==0):
        e_sum=e_sum+a%10
    else:
        o_sum=o_sum+a%10
    a=a//10
    count=count+1
if(e_sum==o_sum):
    print("YES EQUALE")
else:
    print("NOT EQUALE")
