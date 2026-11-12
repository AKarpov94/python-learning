def number(lines):
    a = []
    b = 1
    for i in lines:
        a.append(str(b) +": " +  str(i))
        b = b + 1
    return (a)
print(number(["a","b","c","d"]))

#def number(lines):
#	return [str(x+1) + ": " + lines[x] for x in range(len(lines))]