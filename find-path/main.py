# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as names:
    name_list = names.read().splitlines()

for name in name_list:
    with open(f"Output/ReadyToSend/{name}.txt", "w") as letter:
        with open("Output/ReadyToSend/example.txt") as replace_name:
            content = replace_name.read()
            content = content.replace("Aang", name)
            letter.write(content)
