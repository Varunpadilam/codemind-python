n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i%2==0:
        c+=i
    else :
        d+=i
print(abs(c-d))