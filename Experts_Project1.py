# Open and Read the encrypted text
with open('encrypted_text', 'r+') as file:
    contents = file.read()

# *uncomment* if you want to see the original text
# print(contents) # Prints out the content of Original Unencrypted Text

# Clean special Characters from the Text and normalizing to lower
special_characters = "'.,;->"
cleaned_text = contents
for char in special_characters:
    cleaned_text = cleaned_text.replace(char, "")

cleaned_text_lower = cleaned_text.lower()

print(cleaned_text_lower) # Printing Filtered Text

# Part 4 - Creating an X Shape
size = 7  # Size of the X shape

for i in range(size):
    for j in range(size):
        if i == j or i == size - 1 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Creating a New Dictionary for Characters Count.
def func(cleaned_text_lower):
    char_count_dict = {}
    for char in cleaned_text_lower:
        char_count_dict[char] = char_count_dict.get(char, 0) +1
    return char_count_dict

# Calling the function and sorting the most popular characters
result_dict = func(cleaned_text_lower)
sorted_keys = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[1],reverse=True)}

print(func(cleaned_text_lower)) # printing the dictionary
print(sorted_keys) # printing the sorted keys

lst_four_keys = list(sorted_keys)
print(lst_four_keys[1:5]) #Slicing four keys excluding SPACE

lst_decrypt_vals = ['e', 't', 'o', 'r']
decrypt_dict = {k: v for k, v in zip((lst_four_keys[1:5]),lst_decrypt_vals)}
decrypt_dict2 = {k: v for k, v in zip((lst_decrypt_vals),(lst_four_keys[1:5]))}
decrypt_dict.update(decrypt_dict2)
print(decrypt_dict) #Printing the Dictionary used for Text decryption

decrypted_text = ''.join(decrypt_dict.get(char, char) for char in cleaned_text_lower)
print(decrypted_text)

# Here Is Part 3 of the Project (I didn't understand Part 2)

def func_save_output(file_path):
    with open(file_path, "w+") as file:
        file.write("///This is the Original Text\n")
        file.write(cleaned_text_lower)
        file.write("\n")
        file.write("///This is the Translated Text\n")
        file.write(decrypted_text)
        file.write("\n")

func_save_output(file_path="results.txt")

# Part IV of the Project

import re
regex = re.compile('[^a-zA-Z]')

def func_longestword(file_path):
    """Looks for the Longest Words in the Results.txt Output"""
    with open(file_path, "r+") as file:
        text = file.read()
        word_list = text.split()
        clean_text = []
        for word in word_list:
            clean_word = regex.sub('', word)
            clean_text.append(clean_word)

        longest_words = []
        max_length = 0

        for word in word_list:
            if len(word) > max_length:
                longest_words = [word]
                max_length = len(word)
            elif len(word) == max_length:
                longest_words.append(word)

    print(longest_words)
func_longestword(file_path="results.txt")

# This Function Counts the lines in the results.txt Output File

def func_countlines(file_path):
    line_counter = 0
    with open(file_path, "r+") as file:
        for line in file:
            line_counter += 1

    print("Number of lines:", line_counter)

func_countlines(file_path="results.txt")

