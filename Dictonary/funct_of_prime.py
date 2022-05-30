def prime(n):
    f=0
    for i in range(2,n+1):
        if(n%i==0):
            f+=1
    if(f==1):
        return True
    else:
        return False
s = int(input())
if (prime(s)== True):
    print("Prime")
else:
    print("Not Prime")
