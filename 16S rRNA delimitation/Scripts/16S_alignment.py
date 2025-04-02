import subprocess

def align_sequences(input_file, output_file):
    subprocess.run(["mafft", "--auto", input_file], stdout=open(output_file, "w"))

if __name__ == "__main__":
    input_file = "./data/16S_all_final.fasta"  # Replace with your local path
    output_file = "./data/16S_all_aligned.fasta"  # Replace with your local path
    
    align_sequences(input_file, output_file)
    print("Sequences aligned using MAFFT.")
