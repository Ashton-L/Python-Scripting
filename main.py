import sys
import getpass

while True:

    try:
        password = getpass.getpass("Enter your password (Enter 'exit' to quit): ")
    except KeyboardInterrupt:
        print("\nExiting script due to user interrupt.")
        sys.exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit()

    if password.lower() == "exit":
        sys.exit()

    password_length = len(password)
    if password_length >= 8:
        valid_password = 1
    else:
        print("Password must be 8 characters long")
        continue

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_num = any(char.isnumeric() for char in password)
    has_spec_char = any(not char.isalnum() for char in password)

    if not has_upper or not has_lower or not has_num or not has_spec_char:
        valid_password = 0

    if valid_password == 1:
        print("Valid Password")
    else:
        print("Invalid Password")

    if valid_password == 0:
        if not has_upper:
            print("Password must contain 1 upper case character")
        if not has_lower:
            print("Password must contain 1 lower case character")
        if not has_num:
            print("Password must contain 1 numerical character")
        if not has_spec_char:
            print("Password must contain 1 special character")
