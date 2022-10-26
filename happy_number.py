a=int(input())
b=0
while a>0:
    r=a%10
    b+=r*r
    a=a//10
    if a==0 and b>9:
        a=b
        b=0
if b==1 or b==7:
    print("True")
else :
    print("False")