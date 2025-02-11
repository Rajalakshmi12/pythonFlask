import json

def count_key_occurrences(data, target_key="AWSH"):
    """Recursively count occurrences of the target key in a nested JSON structure."""
    count = 0

    if isinstance(data, dict):  # If it's a dictionary, check its keys
        for key, value in data.items():
            if key == target_key:
                count += 1  # Increment count when key is found
                print(f"{key}: {value}")
            count += count_key_occurrences(value, target_key)  # Recursive call

    elif isinstance(data, list):  # If it's a list, iterate over elements
        for item in data:
            count += count_key_occurrences(item, target_key)  # Recursive call
    return count

json_file_path = "q-extract-nested-json-keys.json"

# Reading from a file
with open (json_file_path, "r") as f:
   json_data = json.load(f)

count = count_key_occurrences(json_data)
print(f"Occurrences of 'AWSH' as a key: {count}")

