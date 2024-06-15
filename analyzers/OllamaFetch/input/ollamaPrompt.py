# https://github.com/dwyl/english-words/blob/master/words.txt

import ollama
import os

def filePath(filename, subfolder="wordfiles"):
    return os.path.join(os.getcwd(), "OllamaFetch", "input", subfolder, filename);

def get_ollama_answer(prompt):
    response = ollama.chat(model='mistral', messages=[
                {'role': 'user','content': prompt,},])
    r1 = response['message']['content']
    return r1

# Read words from a text file (one word per line)
words = []
words_path = filePath("x.txt")
with open(words_path, 'r') as file:
    for line in file:
        # Get the first token (word) from each line
        word = line.strip().split()[0]
        words.append(word)

# Create prompts and get answers from local Ollama
current_path = os.getcwd()
file_path = os.path.join(current_path, "definitions.txt")
print(f"Writing definitions to {file_path}")

with open(file_path, 'w') as file:
    counter = 0
    for word in words:
        counter += 1
        print(f"{counter} {word}")
        prompt = f"Is the word {word} a noun, verb, adjective, adverb, pronoun, preposition, conjunction, or interjection? If it is a verb, please list all of the conjugations. If it is a noun, please list the singular and plural."
        answer = get_ollama_answer(prompt)
        if answer:
            str = f"\n\n'{word}' ==================================\n\n {answer}"
            file.write(str)
        else:
            file.write(f"Failed to get an answer for '{word}' from Ollama.")
