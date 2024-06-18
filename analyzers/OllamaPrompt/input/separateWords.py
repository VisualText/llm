import re
import os

def write_word_file(input_file, word, def_lines):
    letter = get_file_name_without_extension(input_file).replace("-def", "")
    print(f"Writing {word} to {letter} directory")
    write_letter_word_file(letter, word, def_lines)

def create_directories_if_not_exist(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_name_without_extension(file_path):
    base_name = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(base_name)[0]
    
    return file_name_without_extension

def write_letter_word_file(letter, word, lines):
    filename = f"{word}.txt"
    file_path = os.path.join(os.getcwd(), "OllamaPrompt", "input", "wordfiles", letter, filename);
    create_directories_if_not_exist(file_path)
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

def make_word_files(input_file):
    # Read the input file line by line
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Define the pattern: single quote, text, single quote, at least five "="
    pattern = re.compile(r"'([^']+)'\s*={5,}")

    def_lines = []
    word = ''
    foundHeader = False
    # Iterate through the lines
    for line in lines:
        match = pattern.match(line)
        if match:
            if len(def_lines) > 0:
                write_word_file(input_file, word, def_lines)
                def_lines = []

            word = match.group(1)
            foundHeader = True
        elif foundHeader:
            def_lines.append(line)

    if len(def_lines) > 0:
        write_word_file(input_file, word, def_lines)

directory = os.path.join(os.getcwd(), "OllamaPrompt", "input", "wordfiles")
for filename in os.listdir(directory):
    if "-def" in filename:
        file_path = os.path.join(directory, filename)
        make_word_files(file_path)
