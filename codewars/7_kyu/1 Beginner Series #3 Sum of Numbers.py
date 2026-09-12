def get_sum(a,b):
    sum = 0
    while b >= a:
        sum = sum + b
        b = b-1
        print(sum)
    return sum


print(get_sum(1,5))


