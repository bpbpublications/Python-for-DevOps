# Script: 025_encode_categories.py

# List of categories to encode
categories = ['red', 'blue', 'green']

# Creating a dictionary to map each category to a unique integer using dictionary comprehension
encoding = {categories[i]: i for i in range(len(categories))}

# Sample data containing categories to be encoded
data = ['red', 'green', 'blue', 'green']

# Encoding the data by mapping each category to its corresponding integer value
encoded_data = [encoding[item] for item in data]

# Printing the encoded data
print("Encoded data:", encoded_data)
