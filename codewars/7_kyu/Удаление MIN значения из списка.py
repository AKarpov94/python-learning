def remove_smallest(numbers):
    b = numbers.copy()
    if len(numbers) >= 1:
        b.remove(min(b))
        return b
    else:
        return numbers
print(remove_smallest([1,2,1,4,5,6,7,8,9]))
print(remove_smallest([]))

#def remove_smallest(numbers):
#    a = numbers[:]
#    if a:
#        a.remove(min(a))
#    return a

