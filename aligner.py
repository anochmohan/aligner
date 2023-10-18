#!/usr/bin/env python

# Import sys to take in input file
import sys
input_file = sys.argv[1]

# Read the file
with open(input_file, 'r') as i:
    lines = i.read() # produces a list of the lines in the file
    list_wo_n = lines.split("\n")

# Get the needed lines from the list
line_1 = list_wo_n[1]
line_2 = list_wo_n[3]

# variable to store "|" or " "
markers=""

# Loop to check if the indices match
for i in range(0, len(line_1)):
    if line_1[i] == line_2[i]:
        markers += "|"
    else:
        markers += " "

print(line_1)
print(markers)
print(line_2)