import random
import string

def generate_password(length):
    if length < 4:
        return "Error! Password length should be at least 4."

    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)

    # Shuffle the generated password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
