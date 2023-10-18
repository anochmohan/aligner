# aligner

Write a Python script that reads the FASTA file, "aligned.fna" provided on canvas and prints the sequences to
the terminal along with symbols indicating which positions matched. The output of your script should look as
follows: \n
Given the following sequences in a FASTA file, \n
\>seq1 \n
ATGCAAGTCGAGCGGATGAAGGGAGCTTGCTCCTGGATTCAGCGGCGGAC \n
\>seq2 \n
ATGCAAGTCGAGCGGCAGCACAGAGGAACCTTGGGTGGCGAGCGGCGGAC \n
Your script should produce the output \n
ATGCAAGTCGAGCGGATGAAGGGAGCTTGCTCCTGGATTCAGCGGCGGAC \n
||||||||||||||| | | ||| || | |||||||||| \n
ATGCAAGTCGAGCGGCAGCACAGAGGAACCTTGGGTGGCGAGCGGCGGAC \n
Where a pipe symbol is printed between the sequences at positions where the bases are identical, and a space
is printed at positions where the bases differ.
The sequences in the file "aligned.fna" have already been aligned, so you need only process the sequences
and print the output in the described format.
Your script must take command-line input. Do not hard-code the path to the sequence file. The usage of your
script should be
<script name>.py <FASTA file>
