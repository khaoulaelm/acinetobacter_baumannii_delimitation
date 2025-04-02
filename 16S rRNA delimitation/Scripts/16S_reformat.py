# ABGD
import os

def reformat_sequences(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.endswith(".fasta"):
            base = os.path.basename(file).replace(".fasta", "")
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, f"{base}.fasta")
            
            # Reformatting sequences with "copyX" for traceability
            with open(input_file, "r") as infile, open(output_file, "w") as outfile:
                seq_count = 1
                for line in infile:
                    if line.startswith(">"):
                        outfile.write(f">{base}_copy{seq_count}\n")
                        seq_count += 1
                    else:
                        outfile.write(line)

if __name__ == "__main__":
    input_dir = "./data/raw_16S_sequences"  # Replace with your local path
    output_dir = "./data/reformatted_16S_sequences"  # Replace with your local path
    
    reformat_sequences(input_dir, output_dir)
    print("16S sequences reformatted successfully.")
