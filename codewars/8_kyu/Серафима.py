b = 1
c = []
i = 0
while b != 0:
   b = int(input())
   if b != 0:
      c.append(b)
c.sort()
print(c[0]+c[1])
print(c[-1]+c[-2])