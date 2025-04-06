import os
import subprocess

# Path to the ABGD executable
abgd_exec = os.path.expanduser("~/Downloads/Abgd/abgd")  

# Directory containing the aligned core genes (in FASTA format)
input_dir = os.path.expanduser("~/Desktop/article1/GPG_analysis/core_genes_aligned")

# Directory where the ABGD results will be stored
main_output_dir = os.path.expanduser("~/Desktop/article1/GPG_analysis/ABGD_results")

# Ensure output root exists
os.makedirs(main_output_dir, exist_ok=True)

# Loop over each file in the input directory
for fname in os.listdir(input_dir):
    # Skip files that don't end with .fasta (we only want the FASTA files)
    if not fname.endswith(".fasta"):
        continue

    # Get the full path of the current gene alignment file
    gene_path = os.path.join(input_dir, fname)
    
    # Extract the gene name     
    gene_name = os.path.splitext(fname)[0]

    # Create a unique folder for each gene output
    gene_output_dir = os.path.join(main_output_dir, gene_name)
    os.makedirs(gene_output_dir, exist_ok=True)

    # Build the ABGD command
    cmd = [
        abgd_exec,
        "-a",                      # Output all files
        "-o", gene_output_dir,     # Output to this gene-specific folder
        gene_path                  # Input gene alignment
    ]
    
    # Print a message indicating which gene ABGD is currently processing
    print(f"Running ABGD on: {gene_name}")
    
    # Run the ABGD command and wait for it to complete    
    subprocess.run(cmd)

# After all genes are processed, print a final message
print("All genes processed with ABGD.")

