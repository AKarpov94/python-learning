import math
def find_next_square(lst):
    if lst%math.sqrt(lst) != 0:
        return -1
    else:
        return int((math.sqrt(lst) + 1) ** 2)
print(find_next_square(145))

#def find_next_square(sq):
#    root = sq ** 0.5
#    if root.is_integer():
#        return (root + 1)**2
#    return -1

#def find_next_square(sq):
#    x = sq**0.5
#    return -1 if x % 1 else (x+1)**2

#def find_next_square(sq):
#    return (sq**0.5+1)**2 if int(sq**0.5)**2 == sq else -1