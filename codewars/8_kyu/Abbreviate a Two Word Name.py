def abbrev_name(name):
    word = name.upper().split()
    return word[0][0]+"."+word[1][0]
print(abbrev_name("Artem karpov"))

#Решения других
#def abbrevName(name):
    #return '.'.join(w[0] for w in name.split()).upper()
#ИЛИ
#def abbrevName(name):
    #first, last = name.upper().split(' ')
    #return first[0] + '.' + last[0]