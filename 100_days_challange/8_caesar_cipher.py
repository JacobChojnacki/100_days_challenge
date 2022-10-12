from additional_files.art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_amount, direction):
    new_alphabet = [alphabet[x + shift_amount] for x in range(len(alphabet) - shift_amount)]
    new_alphabet.extend([alphabet[x] for x in range(shift_amount)])
    result = ""
    if direction == 'encode':
        for i in plain_text:
            if i in alphabet:
                x = alphabet.index(i)
                result += new_alphabet[x]
            else:
                result += i
    elif direction == 'decode':
        for i in plain_text:
            if i in alphabet:
                x = new_alphabet.index(i)
                result += alphabet[x]
            else:
                result += i
    return f"Here's the {direction}d result: {result}"


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    print(caesar(text, shift, direction))
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if again == 'no':
        print("Goodbye")
        break
