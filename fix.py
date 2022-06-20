def decryptRailFence(cipher, key):

    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))
def encryptRailFence(text, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("".join(result))


e_string = ''
key = "key"
message = "messagetotheman"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Takes erpytion key from user
e_key = key
e_key = e_key.lower()

# Takes string from user
input_string = message
input_string = input_string.lower()

# Lengths of input_string
string_length = len(input_string)

# Expands the eryption key to make it longer than the inputted string
expanded_key = e_key
expanded_key_length = len(expanded_key)

while expanded_key_length < string_length:
    # Adds another repetition of the eryption key
    expanded_key = expanded_key + e_key
    expanded_key_length = len(expanded_key)

key_position = 0

for letter in input_string:
    if letter in alphabet:
        # cycles through each letter to find it's numeric position in the alphabet
        position = alphabet.find(letter)
        # moves along key and finds the characters value
        key_character = expanded_key[key_position]
        key_character_position = alphabet.find(key_character)
        key_position = key_position + 1
        # changes the original of the input string character
        new_position = position + key_character_position
        if new_position > 26:
            new_position = new_position - 26
        new_character = alphabet[new_position]
        e_string = e_string + new_character
    else:
        e_string = e_string + letter
vige = e_string
print("Your Vigenere Encryption of your text is:")
print(vige)
rail_vig_e = ''
rail_vig_d = ''

rail_vig_e = (encryptRailFence(e_string, 3))
rail_vig_d = (decryptRailFence(rail_vig_e, 3))
print("Your Rail Encryption of your Vigenere Encrypted text is:")
print(rail_vig_e)
print("Your Decryption of your Rail & Vig is:")
print(rail_vig_d)
finalstep = (
    "Now that we encrypted Using vig and rail and decrypted the vige rail lets finish with getting our message by putting in the key and cipher")
print(finalstep)






def vig_d():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    d_key = ""
    d_string = ""

    # Takes erpytion key from user
    d_key = input("Please enter eryption key: ")
    d_key = d_key.lower()

    # this is when the string is inputed
    input_string = input("Please enter a string of text: ")
    input_string = input_string.lower()

    # Lengths of the string
    string_length = len(input_string)

    # Expands the eryption key to make it longer than the inputted string
    expanded_key = d_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the eryption key
        expanded_key = expanded_key + d_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            d_string = d_string + new_character
        else:
            d_string = d_string + letter
    return (d_string)

    # This function receives cipher-text
    # and key and returns the original
    # text after decryption

print(key)
print(message)
