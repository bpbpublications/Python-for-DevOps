# Open the file 'example.txt' in append mode
file = open("example.txt", "a")

# Append a new line to the file with the string "Appending this line."
file.write("\nAppending this line.")

# Close the file to ensure changes are saved and the file is properly closed
file.close()
