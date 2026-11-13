def DNA_strand(dna):
    b = str()
    for i in str(dna):
        if i == "A":
            b = str(b) + "T"
        elif i == "T":
            b = str(b) + "A"
        elif i == "C":
            b = str(b) + "G"
        elif i == "G":
            b = str(b) + "C"
    return str(b)
print(DNA_strand(["AATTGGCC"]))


