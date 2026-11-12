def quarter_of(month):
    return 1 if 1<=month<=3 else 2 if 4<=month<=6 else 3 if 7<=month<=9 else 4 if 10<=month<=12 else 0
print(quarter_of(7))

#def quarter_of(n):
#    return (n + 2) // 3