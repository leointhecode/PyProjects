PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    let = letter.read()
    for names in name_list:
        stripped_name = names.strip()
        FLetter = let.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(FLetter)
