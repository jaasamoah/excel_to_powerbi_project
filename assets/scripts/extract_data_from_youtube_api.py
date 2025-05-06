# Import required modules
import os
import sys
import pandas as pd
import numpy as np

# Read data file and return DataFrame
def read_data(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found")
        sys.exit(1)
    # Read CSV and handle headers
    return pd.read_csv(file_path, header=0, encoding='utf-8')

# Clean data by removing missing values
def clean_data(df, threshold=0.3):
    # Drop rows with any missing values
    cleaned_df = df.dropna(axis=0, how='any')
    # Remove columns with too many missing values
    col_threshold = int(threshold * len(cleaned_df))
    return cleaned_df.dropna(axis=1, thresh=col_threshold)

# Calculate summary statistics
def calculate_stats(df):
    # Group by first column and calculate stats
    grouped = df.groupby(df.columns[0])
    stats_df = grouped.agg([np.mean, np.median])
    return stats_df.reset_index()

# Main execution flow
if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    # Process input and output paths
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Execute data pipeline
    data = read_data(input_path)
    cleaned_data = clean_data(data)
    stats = calculate_stats(cleaned_data)
    
    # Save results to output file
    stats.to_csv(output_path, index=False)
    print(f"Analysis saved to {output_path}")
