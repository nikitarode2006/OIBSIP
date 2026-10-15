
import random
import string

print("===== Random Password Generator =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters (A-Z)")
        print("2. Lowercase letters (a-z)")
        print("3. Numbers (0-9)")
        print("4. Symbols (!@#$...)")

        choices = input(
            "Enter choices separated by commas (e.g. 1,2,3): "
        )

        selected = set(choices.replace(" ", "").split(","))

        if not selected or not selected.issubset({"1", "2", "3", "4"}):
            print("Error: Select valid options from 1, 2, 3, 4.")
            continue

        if len(selected) < 2:
            print("Error: Select at least 2 character types.")
            continue

        character_sets = []

        if "1" in selected:
            character_sets.append(string.ascii_uppercase)

        if "2" in selected:
            character_sets.append(string.ascii_lowercase)

        if "3" in selected:
            character_sets.append(string.digits)

        if "4" in selected:
            character_sets.append("!@#$%^&*()-_=+?")

        if length < len(character_sets):
            print("Error: Length is too short for selected types.")
            continue

        # Guarantee at least one character from each selected type
        password_chars = [
            random.choice(characters)
            for characters in character_sets
        ]

        all_characters = "".join(character_sets)

        # Fill the remaining length
        password_chars.extend(
            random.choice(all_characters)
            for _ in range(length - len(password_chars))
        )

        # Shuffle the characters
        random.shuffle(password_chars)

        password = "".join(password_chars)

        print("\nGenerated Password:", password)

        again = input(
            "\nGenerate another password? (yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number for length.")
