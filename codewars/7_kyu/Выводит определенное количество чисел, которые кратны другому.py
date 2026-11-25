def count_by(x, n):
    b = []
    for i in range(1,n+1):
        b.append(i*x)
    return b
print(count_by(1, 10))
print(count_by(2, 10))
print(count_by(1, 3))

#def count_by(x, n):
#    return [i * x for i in range(1, n + 1)]