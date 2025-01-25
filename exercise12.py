import csv

# List of files to process (manually specified)
files = ["file1.csv", "file2.txt", "file3.csv"]  # Add your file names here

# Iterate through files
for filename in files:
    # Handle CSV files
    if filename.endswith(".csv"):
        print(f"Processing CSV file: {filename}")
        with open(filename, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)  # Process each row

    # Handle text files
    elif filename.endswith(".txt"):
        print(f"Processing text file: {filename}")
        with open(filename, mode="r") as text_file:
            for line in text_file:
                print(line.strip())  # Process each line

    # Skip unsupported files
    else:
        print(f"Skipping unsupported file: {filename}")