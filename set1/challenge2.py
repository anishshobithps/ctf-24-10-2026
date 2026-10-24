# Challenge 2: fixed XOR
# This script takes two hex-encoded byte strings, XORs them byte by byte,
# and prints the result in hexadecimal format.
# This function takes two equal-length byte buffers and returns their XOR combination.

def fixed_xor(buffer1, buffer2):
    # Ensure both input byte strings are the same length 
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffers must have equal length")

    # XOR each corresponding byte pair and build the output byte string.
    return bytes(a ^ b for a, b in zip(buffer1, buffer2))

# Read the two hex strings provided by the user.
b1 = input("Enter first hex string: ")
b2 = input("Enter second hex string: ")

# Convert the hex strings into raw bytes.
buffer1 = bytes.fromhex(b1)
buffer2 = bytes.fromhex(b2)

# Apply the XOR operation to both byte arrays.
result = fixed_xor(buffer1, buffer2)

# Print the XOR result as a hex string.
print(result.hex())