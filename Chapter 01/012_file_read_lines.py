# Open the file in read mode

file = open('example.txt', 'r')  # Replace 'example.txt' with the name of your file
# Iterate through each line in the file
for line in file:
    # Print each line (it includes the newline character by default)
    print(line, end='')  # Use `end=''` to avoid double spacing in output
