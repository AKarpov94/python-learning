def digitize(n):
    b = []
    for i in str(n):
        b.append(int(i))
    return b[::-1]
print(digitize(123456))

#def digitize(n):
#    return [int(x) for x in str(n)[::-1]]

#ef digitize(n):
#    return [int(x) for x in reversed(str(n))]