#!/bin/bash

# Create a directory for Prokka results
mkdir -p prokka_results

# Loop through all FASTA files in the data directory
for file in data/*.fasta; do
    base=$(basename "$file" .fasta)  # Get the base name of the file (without the .fasta extension)

    # Run Prokka annotation
    prokka --outdir prokka_results/$base --prefix $base --cpus 4 "$file"
done
