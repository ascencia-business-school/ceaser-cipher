def encrypt(text, shift):
    result = ""  # Initialize the encrypted text
    for char in text:  # Loop through each character in the text
        if char.isalpha():  # Check if the character is alphabetic
            ascii_offset = ord('A') if char.isupper() else ord('a') 
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # Shift the character by the given amount
            result += shifted_char  # Add the shifted character to the encrypted text
        else:
            result += char  # Add the non-alphabetic character to the encrypted text
    return result  # Return the encrypted text


text = "NKRRU CUXRJ" # Original text. This is was encrypted using caesar cipher with shift = 6
shift = 6
result = encrypt(text, shift)  #   encrypt the text
print("Original text:", text) # Print the original text
print("Encrypted text:", result) # Print the encrypted text

# Decryption
e_result = encrypt(text, -shift) # Decrypt the text
print("Decrypted text:", e_result)  # Print the decrypted text
