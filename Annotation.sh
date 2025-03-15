#!/bin/bash

mkdir -p prokka_results

for file in ~/Desktop/article1/genomes/*.fasta; do
    base=$(basename "$file" .fasta)
    prokka --outdir prokka_results/$base --prefix $base --cpus 4 "$file"
done
