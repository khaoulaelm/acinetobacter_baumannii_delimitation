import os

def concatenate_sequences(input_dir, output_file):
    with open(output_file, "w") as outfile:
        for file in os.listdir(input_dir):
            if file.endswith(".fasta"):
                with open(os.path.join(input_dir, file), "r") as infile:
                    outfile.write(infile.read())

if __name__ == "__main__":
    input_dir = "./data/reformatted_16S_sequences"  # Replace with your local path
    output_file = "./data/16S_all_final.fasta"  # Replace with your local path
    
    concatenate_sequences(input_dir, output_file)
    print("All sequences concatenated into 16S_all_final.fasta.")
