import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define input and output paths
asap_matrix_path = os.path.expanduser("~/conspecificity_matrix.csv")
output_path = os.path.expanduser("~/asap_heatmap.png")

# Load ASAP conspecificity matrix
asap_df = pd.read_csv(asap_matrix_path, index_col=0)

# Set up figure size
plt.figure(figsize=(20, 20))

# Generate heatmap with clustering for ASAP
sns.clustermap(asap_df, 
               cmap="coolwarm",  # Better contrast
               linewidths=0.2,   # Add gridlines
               linecolor="black",# Grid color
               cbar_kws={"shrink": 0.5},  # Smaller colorbar
               xticklabels=True,  # Show x labels
               yticklabels=True,  # Show y labels
               figsize=(20, 20),  # Size
               annot=False,       # Set to True if you want numbers in cells
               fmt=".0f",         # No decimals for annotations
               dendrogram_ratio=(0.1, 0.1) # Reduce dendrogram size
              )

# Save heatmap
plt.savefig(output_path, dpi=300)
plt.close()

print(f" ASAP heatmap saved to: {output_path}")

