def correct(s):
    b = str()
    for i in s:
        if i == "0":
            i = 'O'
            b = b + str(i)
        elif i == "1":
            i = 'I'
            b = b + str(i)
        elif i == "5":
            i = 'S'
            b = b + str(i)
        else:
            b = b + str(i)
    return b
print(correct("51NGAP0RE"))

#def correct(string):
#    return string.translate(str.maketrans("501", "SOI"))

#def correct(string):
#    return string.replace('1','I').replace('0','O').replace('5','S')

#tr=str.maketrans('015','OIS')
#def correct(string):
#    return string.translate(tr)