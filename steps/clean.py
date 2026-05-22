def clean(input):
    with open(input, "r") as file:
        valid = True
        cleaned_seq = ""
        cleaned_name = ""
        for line in file:
            if line.startswith(">"):
                cleaned_name += line
            else:
                capitalized = line.upper()
                for i in capitalized:
                    if i in "AGTCN":
                        cleaned_seq += i
        if cleaned_seq == "":
             valid = False
        for i in cleaned_seq:
             if i not in "AGTCN":
                  valid = False
        if valid:
            with open("steps/clean.fasta", "w") as clean_file:
                        clean_file.write(cleaned_name)
                        clean_file.write(cleaned_seq)
        else:
            print("Invalid sequence provided.")
    return(cleaned_name, cleaned_seq)
            