def translate():
    with open("steps/clean.fasta", "r") as file:
        dictionary_codons = {"ATG": "Methionine",
                        "TAA": "Stop",
                        "TAG": "Stop",
                        "TGA": "Stop",

                        "TTT": "Phenylalanine",
                        "TTC": "Phenylalanine",

                        "TTA": "Leucine",
                        "TTG": "Leucine",
                        "CTT": "Leucine",
                        "CTC": "Leucine",
                        "CTA": "Leucine",
                        "CTG": "Leucine",

                        "ATT": "Isoleucine",
                        "ATC": "Isoleucine",
                        "ATA": "Isoleucine",

                        "GTT": "Valine",
                        "GTC": "Valine",
                        "GTA": "Valine",
                        "GTG": "Valine",

                        "TCT": "Serine",
                        "TCC": "Serine",
                        "TCA": "Serine",
                        "TCG": "Serine",
                        "AGT": "Serine",
                        "AGC": "Serine",

                        "CCT": "Proline",
                        "CCC": "Proline",
                        "CCA": "Proline",
                        "CCG": "Proline",

                        "ACT": "Threonine",
                        "ACC": "Threonine",
                        "ACA": "Threonine",
                        "ACG": "Threonine",

                        "GCT": "Alanine",
                        "GCC": "Alanine",
                        "GCA": "Alanine",
                        "GCG": "Alanine",

                        "TAT": "Tyrosine",
                        "TAC": "Tyrosine",

                        "CAT": "Histidine",
                        "CAC": "Histidine",

                        "CAA": "Glutamine",
                        "CAG": "Glutamine",

                        "AAT": "Asparagine",
                        "AAC": "Asparagine",

                        "AAA": "Lysine",
                        "AAG": "Lysine",

                        "GAT": "Aspartic Acid",
                        "GAC": "Aspartic Acid",

                        "GAA": "Glutamic Acid",
                        "GAG": "Glutamic Acid",

                        "TGT": "Cysteine",
                        "TGC": "Cysteine",

                        "TGG": "Tryptophan",

                        "CGT": "Arginine",
                        "CGC": "Arginine",
                        "CGA": "Arginine",
                        "CGG": "Arginine",
                        "AGA": "Arginine",
                        "AGG": "Arginine",

                        "GGT": "Glycine",
                        "GGC": "Glycine",
                        "GGA": "Glycine",
                        "GGG": "Glycine"
                        }
                
        for line in file:
            if line.startswith(">"):
                pass
            else:
                length = len(line)
                start  = False
                protein = []
                for i in range(0, length - 3 + 1):
                    split = line[i:i+3]
                    if split == "ATG":
                        start = True
                        position = i
                if start:
                    for i in range(position, length - 3 + 1, 3):
                        split_prot = line[i:i+3]
                        if "N" in split_prot:
                            protein.append("Unknown")
                        elif split_prot == "TAA" or split_prot == "TGA" or split_prot == "TAG":
                            break
                        else:
                            protein.append(dictionary_codons.get(split_prot))
                short = [name[0] for name in protein]
                short_name = "".join(short)
    return(protein, short_name)
