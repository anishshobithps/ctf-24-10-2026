import base64

###
# This script converts hex strings to base64 strings
# @example
# python challenge1.py
# Enter the hex string : 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Raw Bytes: b"I'm killing your brain like a poisonous mushroom"
# Base 64 String : SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
###

# Hex String to convert to base string
hex_string = input("Enter the hex string : ")

# First we convert to raw bytes as per the instructions given
raw_bytes  = bytes.fromhex(hex_string)
print(f"Raw Bytes : {raw_bytes}")

# Convert to base 64
base64_string = base64.b64encode(raw_bytes).decode("utf-8")

# Print the base 64 string
print(f"Base 64 String : {base64_string}")
