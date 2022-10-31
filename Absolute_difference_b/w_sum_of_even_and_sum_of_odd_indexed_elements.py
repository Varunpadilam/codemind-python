n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==0:
        c+=l[i]
    elif i%2!=0:
        d+=l[i]
print(abs(c-d))