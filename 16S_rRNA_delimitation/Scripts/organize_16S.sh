#!/bin/bash

# Create a directory for reformatted 16S sequences
mkdir -p 16S_all_reformatted

# Loop through all FASTA files in the 16S_seq directory
for file in 16S_seq/*.fasta; do
    base=$(basename "$file" .fasta)  # Get the strain name

    # Renaming the 16S sequences and outputting them into the 16S_all_reformatted folder
    awk -v strain="$base" '
        /^>/ {++i; print ">"strain"_copy"i}  # Rename the sequences with a copy number
        !/^>/ {print}
    ' "$file" > "16S_all_reformatted/${base}.fasta"
done
