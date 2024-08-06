# https://github.com/dwyl/english-words/blob/master/words.txt

import ollama
import os
import re

filename = "s.txt"

def filePath(filename, subfolder="wordfiles"):
    return os.path.join(os.getcwd(), subfolder, filename);
    # return os.path.join(os.getcwd(), "OllamaPrompt", "input", subfolder, filename);

def add_suffix_to_filename(filename, suffix):
    base, ext = filename.rsplit(".", 1)
    new_filename = f"{base}-{suffix}.{ext}"
    return new_filename

def get_ollama_answer(prompt):
    response = ollama.chat(model='mistral', messages=[
                {'role': 'system','content': 'You are a computational linguist. You are asked to provide a definition for a word. Your outputs must be concise and in json format.'},
                {'role': 'user','content': prompt},],
                options = { #'temperature': 1.5, # very creative
                    'temperature': 0 # very conservative (good for coding and correct syntax)
                })
    r1 = response['message']['content']
    return r1

def find_words_done(input_file):
    if not os.path.exists(input_file):
        return []
    
    # Read the input file line by line
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Define the pattern: single quote, text, single quote, at least five "="
    pattern = re.compile(r"\"([^\"]+)\"\s*={5,}")

    words_done = []
    # Iterate through the lines
    for line in lines:
        match = pattern.match(line)
        if match:
           words_done.append(match.group(1))
    return words_done

# Read words from a text file (one word per line)
words = []
words_path = filePath(filename)
with open(words_path, 'r') as file:
    for line in file:
        # Get the first token (word) from each line
        word = line.strip().split()[0]
        words.append(word)

# Create prompts and get answers from local Ollama
suffixname = add_suffix_to_filename(filename, "def")
file_path = filePath(suffixname)

print(f"Writing definitions to {file_path}")
words_done = find_words_done(file_path)

with open(file_path, 'a') as file:
    counter = len(words_done)
    for word in words:
        if word not in words_done:
            counter += 1
            print(f"{counter} {word}")
            prompt = f"Is the word {word} a noun, verb, adjective, adverb, pronoun, preposition, conjunction, or interjection? What human language is this word from? Is this word common or rare? What is the topic area of this word? If it is a verb, please list the infinitive form, and a delineate all of the conjugations. If it is a noun, please deliniate the singular and plural."
            answer = get_ollama_answer(prompt)
            if answer:
                str = f"\n\n\"{word}\" ==================================\n\n {answer}"
                file.write(str)
            else:
                file.write(f"Failed to get an answer for '{word}' from Ollama.")
