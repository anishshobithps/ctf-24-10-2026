###
# This script decrypts a single-byte XOR'd hex string
# @example
# python challenge3.py
# Enter the hex string : 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# Best Key Found : 88 (Character: 'X')
# Decoded Message : Cooking MC's like a pound of bacon
###

# Hex String to decrypt
hex_string = input("Enter the hex string : ")

# First we convert to raw bytes
ciphertext = bytes.fromhex(hex_string)

best_score = 0
best_key = None
decrypted_message = ""

# Common English characters to score the text variations
english_chars = set("etaoinshrdlu ETAOINSHRDLU")

# Try every possible 1-byte key (0 to 255)
for key in range(256):
    # XOR every byte in the ciphertext with the current key
    candidate_bytes = bytes(b ^ key for b in ciphertext)

    try:
        # Convert bytes to a readable string
        candidate_text = candidate_bytes.decode("ascii")

        # Count how many common English letters are in the result
        score = sum(1 for char in candidate_text if char in english_chars)

        # Keep track of the version with the highest score
        if score > best_score:
            best_score = score
            best_key = key
            decrypted_message = candidate_text
    except UnicodeDecodeError:
        continue

# Print the key and the final message
print(f"Best Key Found : {best_key} (Character: '{chr(best_key)}')")
print(f"Decoded Message : {decrypted_message}")
