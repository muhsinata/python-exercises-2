with open("Input/Names/invited_names.txt", "r") as names:
    name_list = names.read().splitlines()

for name in name_list:
    with open(f"Output/ReadyToSend/{name}.txt", "w") as letter:
        with open("Output/ReadyToSend/example.txt") as replace_name:
            content = replace_name.read()
            content = content.replace("Aang", name)
            letter.write(content)
