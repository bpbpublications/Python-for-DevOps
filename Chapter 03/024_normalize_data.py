# Script: 024_normalize_data.py

# Sample data to be normalized
data = [1, 2, 3, 4, 5]

# Finding the minimum and maximum values in the data
min_val, max_val = min(data), max(data)

# Normalizing the data using min-max normalization
# The formula is (x - min) / (max - min)
normalized = [(x - min_val) / (max_val - min_val) for x in data]

# Printing the normalized data
print("Normalized data:", normalized)
