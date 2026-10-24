def score_text(text):
    common = " etaoinshrdluETAOINSHRDLU"
    return sum(text.count(char) for char in common)


def decrypt_single_byte_xor(ciphertext):
    best_text = ""
    best_key = 0
    best_score = 0

    for key in range(256):
        plaintext = bytes(byte ^ key for byte in ciphertext)

        try:
            text = plaintext.decode("ascii")
        except UnicodeDecodeError:
            continue

        score = score_text(text)

        if score > best_score:
            best_score = score
            best_text = text
            best_key = key

    return best_text, best_key, best_score


best_text = ""
best_key = 0
best_score = 0
best_line = 0

with open("4.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        ciphertext = bytes.fromhex(line.strip())

        text, key, score = decrypt_single_byte_xor(ciphertext)

        if score > best_score:
            best_text = text
            best_key = key
            best_score = score
            best_line = line_number

print("Line:", best_line)
print("Key:", hex(best_key))
print("Plaintext:", best_text)