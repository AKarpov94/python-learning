a = 1
b = 0
while a!= 0:
    a = int(input())
    if a%6 == 0 and a%10==4:
        b = b + a
print(b)