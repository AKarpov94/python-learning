def series_sum(n):
    a = float(0)
    b = 1
    for i in range(1, n+1):
        a += float(1/(b))
        b = b + 3
    return (f"{a:.2f}")
print(series_sum(5))

#def series_sum(n):
#    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))