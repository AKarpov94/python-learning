def min_max(lst):
    a =[]
    a.append(min(lst))
    a.append(max(lst))
    return (a)
print(min_max([1,2,3,4,5]))

#def min_max(lst):
#  return [min(lst), max(lst)]

#def min_max(lst):
#  lst.sort()
#  tempor = [lst[0],lst[-1]]
#  return tempor