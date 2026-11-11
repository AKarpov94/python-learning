def find_difference(a, b):
    x = 1
    y = 1
    for i in a:
        x = x * i
    for o in b:
        y = y * o
    return x - y if x > y else y - x
print(find_difference([3, 2, 5], [5, 4, 4]))

#abs() в Python — это встроенная функция, которая возвращает абсолютное значение
#(модуль) переданного числа, то есть значение этого числа без знака минус

#from numpy import prod
#def find_difference(a, b):
#    return abs(prod(a) - prod(b))

#def find_difference(a, b):
#	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])

#def find_difference(a, b):
#	return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

#import math
#def find_difference(a, b):
#    return abs(math.prod(a)-math.prod(b))