# Open the file 'example.txt' in read mode using the `with` statement
with open("example.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()
    # Print the content of the file
    print(content)
