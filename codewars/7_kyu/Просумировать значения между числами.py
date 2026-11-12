def get_sum(a,b):
    c=0
    if a < b:
        for i in range(a,b+1):
            c = c + i
    elif a > b:
        for i in range(b,a+1):
            c = c + i
    else:
        return a
    return c
print(get_sum(2,5))

#def get_sum(a,b):
#    return sum(range(min(a, b), max(a, b) + 1))

#def get_sum(a, b):
#    return (a + b) * (abs(a - b) + 1) // 2