# bio-pipe

## what does it do:
  - simple biopipeline tool that inputs a dna sequence and cleans it.
  - then using the --steps flag user can select any function in combination or all together from one of these:
    - clean
    - analyze
    - reversecomplement
    - translate
  - gives the output in a user desired foled as report.txt and translation.txt

## how to set up:
  - no modules needed
  - runs on python 3
  - terminal command will look like this:
    ``` python pipeline.py --input input/sample.fasta --steps clean analyze reversecomplement translate --output output\ ```

## terminal command and ouput files gif:
<img width="1920" height="1080" alt="gif_terminal" src="https://github.com/user-attachments/assets/4bdef161-75e5-4c82-af50-5175fb37b603" />
