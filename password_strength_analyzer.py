import re
# Heading
print("=" * 55)
print("             PASSWORD STRENGTH ANALYZER")
print("=" * 55)
# Common passwords
common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "admin123",
    "welcome",
    "welcome123",
    "letmein",
    "abc123",
    "iloveyou"
]
# Predictable sequences
sequences = [
    "1234567890",
    "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]
while True:
    password = input("\nEnter your password: ")
    score = 0
    suggestions = []
    lower_password = password.lower()
    length = len(password)
    # 1. Password length
  
    if length >= 16:
        score += 2
    elif length >= 12:
        score += 1
    else:
        suggestions.append(
            "Use at least 12 characters. 16 or more is better."
        )

    # 2. Uppercase letter

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    # 3. Lowercase letter

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter."
        )
  
    # 4. Number
 
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one number."
        )

    # 5. Special character

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one special character."
        )

    # 6. Character variety

    character_types = 0

    if re.search(r"[A-Z]", password):
        character_types += 1

    if re.search(r"[a-z]", password):
        character_types += 1

    if re.search(r"[0-9]", password):
        character_types += 1

    if re.search(r"[^A-Za-z0-9]", password):
        character_types += 1


    if character_types == 4:
        score += 1
    else:
        suggestions.append(
            "Use a combination of uppercase, lowercase, numbers and symbols."
        )
  
    # 7. Check repeated characters


    repeated = re.search(r"(.)\1\1", password)

    if not repeated:
        score += 1
    else:
        suggestions.append(
            "Avoid repeating the same character 3 or more times."
        )

    # 8. Check predictable sequences

    sequence_found = False

    for sequence in sequences:

        for i in range(len(sequence) - 2):

            part = sequence[i:i + 3]

            if part in lower_password:
                sequence_found = True
                break

        if sequence_found:
            break


    if not sequence_found:
        score += 1
    else:
        suggestions.append(
            "Avoid predictable sequences such as abc, 123 or qwerty."
        )

    # 9. Check common password
 

    if lower_password not in common_passwords:
        score += 1
    else:
        suggestions.append(
            "This is a commonly used password. Choose a unique password."
        )

    # 10. Check password diversity


    unique_characters = len(set(password))

    if length > 0 and unique_characters / length >= 0.60:
        score += 1
    else:
        suggestions.append(
            "Use more different characters instead of repeating characters."
        )

    # Make sure score stays between 0 and 10


    score = max(0, min(score, 10))
  
    # Determine strength

    if score >= 9:
        strength = "VERY STRONG"

    elif score >= 7:
        strength = "STRONG"

    elif score >= 5:
        strength = "MEDIUM"

    elif score >= 3:
        strength = "WEAK"

    else:
        strength = "VERY WEAK"

    # Display result
 
    print("\n" + "=" * 55)
    print("                 PASSWORD ANALYSIS")
    print("=" * 55)

    print("Password Length :", length)
    print("Security Score  :", score, "/ 10")
    print("Strength        :", strength)

    # Character analysis

    print("\nCharacter Analysis")
    print("-" * 30)

    print(
        "Uppercase       :",
        "Yes" if re.search(r"[A-Z]", password) else "No"
    )

    print(
        "Lowercase       :",
        "Yes" if re.search(r"[a-z]", password) else "No"
    )

    print(
        "Numbers         :",
        "Yes" if re.search(r"[0-9]", password) else "No"
    )

    print(
        "Special Chars   :",
        "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No"
    )

    print(
        "Repeated Chars  :",
        "Yes" if repeated else "No"
    )

    print(
        "Common Password :",
        "Yes" if lower_password in common_passwords else "No"
    )

    print(
        "Sequence Found  :",
        "Yes" if sequence_found else "No"
    )

    # Suggestions

    if suggestions:

        print("\nSuggestions")
        print("-" * 30)

        for suggestion in suggestions:
            print("•", suggestion)

    else:

        print("\nExcellent!")
        print("Your password passed all security checks.")


    # Check another password

    choice = input(
        "\nDo you want to analyze another password? (yes/no): "
    )

    if choice.lower() not in ["yes", "y"]:

        print("\nThank you for using Password Strength Analyzer!")
        print("Stay secure!")
        break




  