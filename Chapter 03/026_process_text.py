# Script: 026_process_text.py

# Importing the string module for punctuation handling
import string

# Sample text to process
text = "Hello, World! This is a test."

# Converting the text to lowercase and removing punctuation using str.translate
# str.maketrans('', '', string.punctuation) creates a translation table to remove all punctuation
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# Splitting the text into individual words
words = text.split()

# Printing the list of words after processing
print("Words:", words)
