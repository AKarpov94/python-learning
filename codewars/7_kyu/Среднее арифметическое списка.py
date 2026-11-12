def find_average(numbers):
    sum = 0
    if numbers == []:
        return 0
    else:
        for i in numbers:
            sum = sum + i
    return sum / len(numbers)
print(find_average([3,5]))

#def find_average(array):
#    return sum(array) / len(array) if array else 0

#def find_average(array):
#    try:
#        return sum(array) / len(array)
#    except ZeroDivisionError:
#       return 0