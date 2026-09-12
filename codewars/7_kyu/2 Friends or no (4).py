def friend(x):
    fr = []
    for i in x:
        if len(i) == 4:
            fr.append(i)
    return fr
print(friend(["Ryan", "Kieran", "Mark", "Ryan", "Mark"]))
#def friend(x):
#    return [f for f in x if len(f) == 4]