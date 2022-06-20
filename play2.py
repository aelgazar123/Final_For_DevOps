import itertools
import string


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


def main():
    text = input("Enter Text: ")
    typeOfText = input("Is this plain text? (y/n) ")

    key1 = input("Affine key1: ")
    key2 = input("Affine key2: ")
    key3 = input("Enter keyword: ")

    keyMatrix = [int(key1), int(key2)]
    print(keyMatrix)
    typeOfText.lower().strip()

    if typeOfText == "y":
        # Playfair then affine because play fair has to be first
        affine = PlayFairencrypt(text, key3)
        print("The alfine Cipher of your message is")
        print(affine)
        print(affine_encrypt(affine, keyMatrix))
    elif typeOfText == "n":
        # affine then Playfair
        playfair = affine_decrypt(text, keyMatrix)
        print("J's will be returned as I: " + PlayFairdecrypt(playfair, key3))


if __name__ == '__main__':
    main()