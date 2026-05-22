def reverse_comp():
    with open("steps/clean.fasta", "r") as file:
        comp = ""
        for line in file:
            if line.startswith(">"):
                pass
            else:
                for i in line:
                    if i == "A":
                        comp += "T"
                    elif i == "T":
                        comp += "A"
                    elif i == "G":
                        comp += "C"
                    elif i == "C":
                        comp += "G"
                    else:
                        comp += "N"
        reverse_complement = comp[::-1]
    return reverse_complement
