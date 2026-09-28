# Password Strength Checker
# This program checks a password without saving or displaying it.

def check_password(password):
    """Return a strength label and a list of suggestions."""
    suggestions = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not has_upper:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not has_lower:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not has_digit:
        suggestions.append("Add at least one number (0-9).")
    if not has_special:
        suggestions.append("Add at least one special character, such as ! or #.")

    # This is a simple classroom checker, not a complete security test.
    checks_passed = sum([
        len(password) >= 8,
        has_upper,
        has_lower,
        has_digit,
        has_special
    ])

    if checks_passed <= 2:
        strength = "Weak"
    elif checks_passed <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    """Get a password and print its strength and suggestions."""
    print("Password Strength Checker")
    print("-------------------------")
    password = input("Enter a password to check: ")

    strength, suggestions = check_password(password)
    print(f"\nPassword strength: {strength}")

    if suggestions:
        print("Suggestions to improve it:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password meets all the checks in this program.")

    print("\nNote: This program does not save your password.")


if __name__ == "__main__":
    main()
