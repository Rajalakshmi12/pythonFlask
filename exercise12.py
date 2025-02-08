import csv
from charset_normalizer import detect
import pandas as pd

#Checking githubc

sum = 0
# List of files to process (manually specified)
files = ["data2.csv"]  # Add your file names here

# Iterate through files
for filename in files:
    # Handle CSV files
    if filename.endswith(".csv"):
        print(f"Processing CSV file: {filename}")
        with open(filename, errors='replace') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] in ["ˆ", "™", "—"]:
                    sum += int(row[1])
            print(f"Sum until now: {sum}")

    # Handle text files
    elif filename.endswith(".txt"):
        print(f"Processing text file: {filename}")
        df = pd.read_csv(filename, delim_whitespace=True, encoding='utf-16')
        for index, row in df.iterrows():
            if row['symbol'] == "ˆ":
                print(f"symbol={row['symbol']} value={row['value']}")
                sum += row['value']
            elif row['symbol'] == "™":
                sum += row['value']
            elif row['symbol'] == "—":
                sum += row['value']
        print(f"Sum until now: {sum}")

    # Skip unsupported files
    else:
        print(f"Skipping unsupported file: {filename}")