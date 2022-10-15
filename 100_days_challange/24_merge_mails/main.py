with open('./Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()
with open('./Input/Names/invited_names.txt') as file_names:
    names = file_names.readlines()

for name in names:
    replaced_name = starting_letter.replace("[name]", name.strip())
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', 'w') as output:
        output.write(replaced_name)


# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
