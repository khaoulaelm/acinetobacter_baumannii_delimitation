import os
import subprocess

abgd_exec = os.path.expanduser("~/Downloads/Abgd/abgd")  # Correct ABGD binary path
input_dir = os.path.expanduser("~/Desktop/article1/GPG_analysis/core_genes_aligned")
main_output_dir = os.path.expanduser("~/Desktop/article1/GPG_analysis/ABGD_results")

# Ensure output root exists
os.makedirs(main_output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if not fname.endswith(".fasta"):
        continue

    gene_path = os.path.join(input_dir, fname)
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

    print(f" Running ABGD on: {gene_name}")
    subprocess.run(cmd)

print("All genes processed with ABGD.")

