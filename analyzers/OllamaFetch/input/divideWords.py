import os
import re

def filePath(filename, subfolder="wordfiles"):
    return os.path.join(os.getcwd(), "OllamaFetch", "input", subfolder, filename);

def has_punctuation(word):
    # Define a regex pattern to match punctuation (excluding dashes and apostrophes)
    pattern = r"[^\w'-]"

    # Check if the word contains any punctuation
    return bool(re.search(pattern, word))

# Read the content of the "words.txt" file
file_path = filePath("words.txt","")
with open(file_path, "r") as file:
    words = file.read().splitlines()

# Initialize dictionaries to store words
capitalized_words = []
other_words = {}

# Separate capitalized words and other words
for word in words:
    firstletter = word[0]
    if firstletter.isupper():
        capitalized_words.append(word)
    elif firstletter.islower() and firstletter.isalpha() and not has_punctuation(word):
        first_letter = word[0].lower()
        if first_letter not in other_words:
            other_words[first_letter] = []
        other_words[first_letter].append(word)

# Write capitalized words to "caps.txt"
caps_path = filePath("caps.txt")
with open(caps_path, "w") as caps_file:
    caps_file.write("\n".join(capitalized_words))

# Write other words to separate files
for letter, word_list in other_words.items():
    filename = f"{letter}.txt"
    file_path = filePath(filename)
    with open(file_path, "w") as other_file:
        other_file.write("\n".join(word_list))

print("Words have been categorized and saved to files as requested.")
