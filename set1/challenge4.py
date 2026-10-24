###
# This script identifies the most likely single-byte XOR key for each line in a file
# by trying all 256 keys and scoring each decrypted result for English-like text.
# 
# OUTPUT
# python challenge4.py
# Line: 170
# Key: 0x1b
# Plaintext: "Now that the party is jumping"
###

# Score a candidate plaintext based on how many common English letters and spaces it contains.
def score_text(text):
    common = " etaoinshrdluETAOINSHRDLU"
    return sum(text.count(char) for char in common)


# Try every possible single-byte XOR key and keep the plaintext with the highest score.
def decrypt_single_byte_xor(ciphertext):
    best_text = ""
    best_key = 0
    best_score = 0

    for key in range(256):
        # XOR every byte in the ciphertext with the current key.
        plaintext = bytes(byte ^ key for byte in ciphertext)

        # Keep only values that decode as ASCII text.
        try:
            text = plaintext.decode("ascii")
        except UnicodeDecodeError:
            continue

        # Score the candidate plaintext using common English character frequency.
        score = score_text(text)

        # Track the best result so far for this ciphertext.
        if score > best_score:
            best_score = score
            best_text = text
            best_key = key

    # Return the most likely plaintext, key, and its heuristic score.
    return best_text, best_key, best_score


# Track the globally best decrypted string across all lines in the input file.
best_text = ""
best_key = 0
best_score = 0
best_line = 0

# Read each hex-encoded ciphertext line from the challenge file.
with open("4.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        # Convert the text line into raw bytes.
        ciphertext = bytes.fromhex(line.strip())

        # Decrypt the current line with each possible single-byte key.
        text, key, score = decrypt_single_byte_xor(ciphertext)

        # Keep the line whose plaintext appears most English-like.
        if score > best_score:
            best_text = text
            best_key = key
            best_score = score
            best_line = line_number

# Print the winning line number, key, and resulting plaintext.
print("Line:", best_line)
print("Key:", hex(best_key))
print("Plaintext:", best_text)