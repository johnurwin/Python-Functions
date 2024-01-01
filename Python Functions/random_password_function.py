# let's create a Python function that generates a random password with a specified length, combining uppercase and lowercase letters, numbers, and special characters.
# We'll use the secrets module for better security in generating random values.

import secrets
import string

def generate_password(length=12):
    """
    Generate a random password with a specified length.

    Parameters:
    - length (int): Length of the password (default is 12).

    Returns:
    - str: Random password.
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 4
    length = max(length, 4)

    # Generate the password using secure random choices
    password = ''.join(secrets.choice(all_characters) for _ in range(length))

    return password

# Example usage:
random_password = generate_password()
print("Random Password (Default Length of 12):", random_password)

# Example usage 2:
random_password_25 = generate_password(25)
print("Random Password (Specified Length of 25):", random_password_25)

