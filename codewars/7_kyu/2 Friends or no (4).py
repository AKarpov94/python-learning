def friend(x):
    fr = []
    for i in x:
        if len(i) == 4:
            fr.append(i)
    return fr
print(friend(["Ryan", "Kieran", "Mark", "Ryan", "Mark"]))