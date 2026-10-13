n=int(input())
r=""
while n>0:
    r=str(n%2)+r
    n=n//2
print(r)