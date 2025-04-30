def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i, line in enumerate(file, start=1):
                print("Line ",i,':', line.strip())
    except FileNotFoundError:
        print("Error: The file ",filename," was not found.")

# Run the function
read_file('sample.txt')
