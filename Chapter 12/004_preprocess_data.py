# Script: 004_preprocess_data.py

import pandas as pd

# Example preprocessing steps
def preprocess(data_path, output_path):
    """
    Preprocess the data from the input file and save the preprocessed data to the output file.
    
    Args:
        data_path (str): Path to the input CSV file.
        output_path (str): Path to save the preprocessed CSV file.
    """
    # Load the data
    data = pd.read_csv(data_path)
    
    # Example preprocessing: Remove duplicates and handle missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    data = data.fillna(method='ffill')  # Fill missing values with forward fill (or adjust as needed)
    
    # Save the preprocessed data
    data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to: {output_path}")

if __name__ == "__main__":
    preprocess('input_data.csv', 'preprocessed_data.csv')
