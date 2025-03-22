# Script: 023_replace_none_with_mean.py

# Assuming missing values are represented as None
# Importing the necessary module for handling None values
data = [10, 20, None, 30]

# Calculating the mean of the data, excluding None values using filter() and summing the result
avg = sum(filter(None, data)) / len(list(filter(None, data)))  # Calculating mean

# Replacing None values with the calculated mean using a list comprehension
data = [x if x is not None else avg for x in data]  # Replacing None with mean

# Printing the updated data with None values replaced by the mean
print("Updated data:", data)
