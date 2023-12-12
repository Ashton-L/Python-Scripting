#This is a simple Caesar Cipher script.  It allows for both encrypting and decrypting messages with a custom rotation value.

import sys


def encrypt():
    new_statement = ""
    for char in message:
        if not char.isalpha() and char != " ":
            raise ValueError("Message must contain only letters and spaces")
        if char.isalpha():
            new_char_code = ord(char) + shift
            if char.islower():
                new_char_code = (new_char_code - ord('a')) % 26 + ord('a')
            elif char.isupper():
                new_char_code = (new_char_code - ord('A')) % 26 + ord('A')
            new_char = chr(new_char_code)
            new_statement += new_char
        else:
            new_statement += char
    print(f'Encoded Statement: {new_statement}')


def decrypt():
    new_statement = ""
    for char in message:
        if not char.isalpha() and char != " ":
            raise ValueError("Message must contain only letters and spaces")
        if char.isalpha():
            new_char_code = ord(char) - shift
            if char.islower():
                new_char_code = (new_char_code - ord('a')) % 26 + ord('a')
            elif char.isupper():
                new_char_code = (new_char_code - ord('A')) % 26 + ord('A')
            new_char = chr(new_char_code)
            new_statement += new_char
        else:
            new_statement += char
    print(f'Decoded Statement: {new_statement}')


while True:
    try:
        process = str(input("Encrypt or Decrypt? (Enter 'exit' to quit): ")).lower()
        if process == 'exit':
            sys.exit()
        if process == "encrypt":
            message = str(input("Statement to encrypt: "))
            shift = int(input("Enter numerical shift value: "))
            encrypt()
            continue
        elif process == "decrypt":
            message = str(input("Statement to decrypt: "))
            shift = int(input("Enter numerical shift value: "))
            decrypt()
            continue
        else:
            print("Invalid selection; Try again.")
    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print("Exiting script due to user interrupt.")
    except Exception as e:
        print(f'Unknown exception: {e}')
