def digitize(n):
    result = []

    for i in str(n):
        result.append(int(i))

    return result[::-1]
print(digitize(35231))