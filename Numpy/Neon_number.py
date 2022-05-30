num=int(input("Enter the number"))
sum=0
a=num*num
while(a>0):
  digit=a%10
  sum=sum+digit
  a=a//10
if(sum==num):
  print("Neon number")
 else:
  print("Not a neon number")
