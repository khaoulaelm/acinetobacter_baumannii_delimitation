#!/bin/bash

# Step 1: Prepare the GFF Files
mkdir -p gff_files
# Copy all GFF files from Prokka results to a single directory
cp prokka_results/*/*.gff gff_files/

# Step 2: Run Roary with default parameters
mkdir -p roary_results
roary -e --mafft -p 8 -f roary_results gff_files/*.gff

# Step 3: Create the tree in Newick format using FastTree
FastTree -nt roary_results/core_gene_alignment.aln > roary_results/tree.newick

# Step 4: Visualize results using Python plotting script
python3 roary_plots.py --labels roary_results/tree.newick roary_results/gene_presence_absence.csv
