a=int(input())
b=int(input())
x=0
y=0
for i in range(1,a):
    if a%i==0:
        x+=i
for c in range(1,b):
    if b%c==0:
        y+=c
if x==b and y==a:
    print("Amicable")
else :
    print("Not Amicable")