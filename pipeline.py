import os
import argparse
from steps.clean import clean
from steps.translate import translate
from steps.analyze import analyze
from steps.reversecomplement import reverse_comp

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="path to fasta file.")
parser.add_argument("--steps", nargs="+", help="steps to run.")
parser.add_argument("--output", help="output folder.")

args = parser.parse_args()
os.makedirs(args.output, exist_ok= True)
report = os.path.join(args.output, "report.txt")
translation = os.path.join(args.output, "translation.txt")

for i in args.steps:
    if i == "clean":
        cleaned_name, cleaned_seq = clean(args.input)
    if i == "analyze":
        sequence_length,unknown, gc_content,a,t,g,c,a_content,c_content,g_content,t_content = analyze()
    if i == "translate":
        protein, short_name = translate()
    if i == "reversecomplement":
        reverse_complement = reverse_comp()

with open(report, "w") as file:
    file.write("=========REPORT=========\n")
    if "clean" in args.steps:
        file.write(f"Name: {cleaned_name}sequence: {cleaned_seq} \n")
    if "analyze" in args.steps:
        file.write(f"The length of the sequence is: {sequence_length} bp.\nThe unknown bases count is: {unknown}.\nThe GC content is: {round(gc_content, 2)}%.\nNumber of bases A: {a},T: {t},G: {g},C:{c}.\nPercentage of A,T,G,C respectively: {a_content}% ,{t_content}%, {g_content}%, {c_content}%.\n"
)
    if "reversecomplement" in args.steps:
        file.write(f"Reverse complement of sequence: {reverse_complement}\n")
    if "translate" in args.steps:
        file.write(f"Translated protein is: {protein}\nShort version: {short_name}")

with open(translation, "w") as file:
    if "translate" in args.steps:
        file.write(short_name)