# Imports
# -----------------------------------------------------------
import itertools
import string

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import datasets
import numpy as np
from IPython.display import Image
from sklearn.cluster import KMeans
import pandas as pd
import base64


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


def prepare_input(text):
    text = "".join([c.upper() for c in text if c in string.ascii_letters])
    clean = ""

    if len(text) < 2:
        return text

    for i in range(len(text) - 1):
        clean += text[i]

        if text[i] == text[i + 1]:
            clean += "X"

    clean += text[-1]

    if len(clean) & 1:
        clean += "X"

    return clean


def removeXs(text):
    text = "".join([c.upper() for c in text if c in string.ascii_letters])
    clean = ""

    for i in range(len(text) - 1):
        if text[i] == "X" and text[i - 1] == text[i + 1]:
            continue
        clean += text[i]

    return clean


def createchunk(text, size):
    it = iter(text)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def removeJ(text):
    text = "".join([c.upper() for c in text if c in string.ascii_letters])
    clean = ""
    for i in range(len(text)):
        if text[i] == "J":
            clean += "I"
            continue
        clean += text[i]

    return clean


def PlayFairencrypt(text, key):
    text = removeJ(text)
    table = generateKeyTable(key)
    plaintext = prepare_input(text)
    ciphertext = ""

    for char1, char2 in createchunk(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]

    return ciphertext


def PlayFairdecrypt(text, key):
    text = removeJ(text)
    table = generateKeyTable(key)
    plaintext = ""

    for char1, char2 in createchunk(text, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # rectangle
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]

    plaintext = removeXs(plaintext)

    return plaintext


def generateKeyTable(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in keyword.lower():
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    return table


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def affine_encrypt(text, key):
    return ''.join(
        [chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


def affine_decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])


st.image('crypto.png')
st.title("CIPHER DESIGN")

st.write("""LETS DO SOME ENCRYPTING STARTING WITH OUR FIRST CIPHER AFFINE..........""")
message = st.text_input("Enter your affine message")
st.write("Affine Message.......................", message)

key1 = st.text_input("Enter your First Affine key")
st.write("Affine key 1.......................", key1)

key2 = st.text_input("Enter your Second Affine key")
st.write("Affine key 2.......................", key2)

key3 = st.text_input("Enter key")
st.write("Affine key.......................", key3)

option = st.selectbox('Is this Plaintext or Ciphertext', ('_','Decrypt', 'Encrypt'))
key1=1
key2=2
keyMatrix = [int(key1), int(key2)]
st.write(keyMatrix)
message.lower().strip()
if option == 'Encrypt':
    st.write('You selected:', option)

    # Playfair then affine because play fair has to be first
    affine = PlayFairencrypt(message, key3)
    st.write("The alfine cipher of your message is")
    st.write(affine)
    aff_play = (affine_encrypt(affine, keyMatrix))
    st.write("The affine..playfair cipher of your messageis")
    st.write(aff_play)

    e_key = ""
    vig1 = ""
    e_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    # Takes erpytion key from user
    e_key = st.text_input(
        "Now Lets Do Vig encryption of affine..playfair cipher enter any key and we will use your prevous encryption to encrypt further")
    e_key = e_key.lower()
    st.write("Your Vig key is....................", e_key)
    st.write(e_key)
    aff_play = aff_play.lower()
    string_length = len(aff_play)
    st.write("help")
    expanded_key = e_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the eryption key
        expanded_key = expanded_key + e_key
        expanded_key_length = len(expanded_key)
    key_position = 0

    for letter in aff_play:
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
    st.image('vigetxt.png', caption=None, width=200)
    st.caption("""Your Vigenere Encryption of your text is:""")
    st.subheader(vige)
    rail_vig_e = ''
    rail_vig_d = ''
elif option == 'Decrypt':
    st.write("dcrypt")
else:
    st.write("bye")