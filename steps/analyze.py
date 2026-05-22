def analyze():
    with open("steps/clean.fasta", "r") as file:
        sequence_length = a = t = g = c = unknown = 0
        for line in file:
            if line.startswith(">"):
                pass
            else:
                for i in line:
                    if i == "G":
                        g += 1
                    elif i == "A":
                        a += 1
                    elif i == "T":
                        t += 1
                    elif i == "C":
                        c += 1
                    elif i == "N":
                        unknown += 1

                sequence_length = a + t + g + c + unknown
                gc_content = ((g+c)/sequence_length) * 100
                a_content = (a/sequence_length) * 100
                t_content = (t/sequence_length) * 100
                g_content = (g/sequence_length) * 100
                c_content = (c/sequence_length) * 100
                
    return(sequence_length,unknown,gc_content,a,t,g,c,a_content,c_content,g_content,t_content)