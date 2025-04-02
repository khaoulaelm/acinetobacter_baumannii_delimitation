import subprocess

def run_abgd(input_file, output_dir):
    subprocess.run(["./abgd", "-a", "-o", output_dir, "-d", "JC69", input_file])

def run_asap(input_file, output_dir):
    subprocess.run(["./asap", "-u", "-o", output_dir, input_file])

if __name__ == "__main__":
    input_file = "./data/16S_all_aligned.fasta"  # Replace with your local path
    abgd_output_dir = "./abgd_output_all"  # Replace with your local path
    asap_output_dir = "./asap_output_all"  # Replace with your local path
    
    # Run ABGD
    run_abgd(input_file, abgd_output_dir)
    
    # Run ASAP
    run_asap(input_file, asap_output_dir)
    
    print("ABGD and ASAP analyses completed.")
