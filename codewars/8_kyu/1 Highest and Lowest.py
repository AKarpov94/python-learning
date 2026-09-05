#Это для себя
def high_and_low(numbers):
    numbers = numbers.split()
    a = int(numbers[0])
    b = int(numbers[0])
    for n in numbers:
        n = int(n)
        if n > a:
            a = n
        elif n < b:
            b = n
    return [a,b]

print(high_and_low(input()))
#Это для платформы
def high_and_low(numbers):
    numbers = numbers.split()
    a = int(numbers[0])
    b = int(numbers[0])
    for n in numbers:
        n = int(n)
        if n > a:
            a = n
        elif n < b:
            b = n
    return str(a) + ' ' +  str(b)
#def high_and_low(numbers): #z.
#    nn = [int(s) for s in numbers.split(" ")]
#    return "%i %i" % (max(nn),min(nn))