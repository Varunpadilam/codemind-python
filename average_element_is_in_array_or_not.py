n=int(input())
l=list(map(int,input().split()))
c=sum(l)//n
if c not in l :
    print("False")
else :
    print("True")