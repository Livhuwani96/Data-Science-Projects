
# Create a variable called user_sentence.
# Request user to input any sentence of choice.

user_sentence = input("Enter a sentence: ")

# Initialize an empty string to store the modified sentence
modified_sentence = ""

# Start by capitalizing the first character
capitalize_next = True

# Process each character in the input sentence
for char in user_sentence:
    if capitalize_next:
        # Convert to uppercase
        modified_sentence += char.upper()
    else:
        # Convert to lowercase
        modified_sentence += char.lower()
    # Toggle the flag for the next character
    capitalize_next = not capitalize_next

# Print the alternate case sentence
print("Alternate case sentence:", modified_sentence)


# This is the second part of the task
# Create a program called alternative.py

# Read input from the user
user_sentence = input("Enter a sentence: ")

# Split the sentence into words
words = user_sentence.split()

# Initialize an empty list to store the modified words
modified_words = []

# Process each word
for i, word in enumerate(words):
    if i % 2 == 0:
        # Convert even-indexed words to lowercase
        modified_words.append(word.lower())
    else:
        # Convert odd-indexed words to uppercase
        modified_words.append(word.upper())

# Join the modified words to form the alternate word case sentence
alternate_word_case = ' '.join(modified_words)

# Print the result
print("Alternate word case sentence:", alternate_word_case)
