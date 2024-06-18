import os

# Define the directory path
directory_path = os.path.join(os.getcwd(), "OllamaPrompt", "input", "wordfiles");

# Initialize a list to store file names
matching_files = []

# Iterate over files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, "r") as file:
            if "def" not in file_path:
                # Append the file name to the list
                matching_files.append(filename)

# Print the matching files and their line counts
files = [];
total_lines = 0
for filename in matching_files:
    file_path = os.path.join(directory_path, filename)
    with open(file_path, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        files.append((filename, line_count))
        total_lines += line_count

# Sort the list by line count (lowest to highest)
files.sort(key=lambda x: x[1])

# Print the sorted file info
print(f"Total lines: {total_lines}")
for filename, line_count in files:
    print(f"File: {filename}, Lines: {line_count}")