def sort_by_length(arr):
    arr.sort(key=len)
    print(arr)
print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))

# Тут н еизменен первоначальный список
#def sort_by_length(arr):
#    return sorted(arr, key=len)
