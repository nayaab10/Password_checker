# Project Statement — Password Strength Checker 🔐

## 1. Project Title

**Password Strength Checker**

---

## 2. Problem Statement

Passwords are commonly used to protect accounts and personal information. However, users often create passwords that are short, predictable, or lack a combination of different character types.

A weak password may be easier to guess than a password containing a suitable combination of letters, numbers, and special characters.

The objective of this project is to develop a simple Python program that checks the basic characteristics of a password and provides the user with feedback about its strength.

The program evaluates the password based on five basic requirements:

1. Minimum length of 8 characters.
2. At least one uppercase letter.
3. At least one lowercase letter.
4. At least one numerical digit.
5. At least one special character.

The program then classifies the password as **Weak, Medium, or Strong** according to the number of requirements satisfied.

---

## 3. Aim

To develop a beginner-friendly Python program that evaluates the basic strength of a password using character analysis and conditional logic.

---

## 4. Objectives

The objectives of this project are:

* To develop a practical application using Python.
* To understand the use of functions.
* To practice loops and conditional statements.
* To work with strings and individual characters.
* To use Boolean variables for tracking conditions.
* To use lists for storing suggestions.
* To provide useful feedback based on program conditions.
* To understand basic time and space complexity.
* To demonstrate how programming concepts can be applied to a real-world problem.

---

## 5. Scope of the Project

The scope of this project is limited to a basic rule-based password evaluation system.

The program checks whether the password contains:

* Sufficient length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

The program also provides suggestions whenever one or more requirements are not satisfied.

This project is primarily intended for **learning Python programming concepts** and understanding how multiple conditions can be combined to solve a practical problem.

---

## 6. Proposed Solution

The proposed solution is a Python program that accepts a password from the user and analyzes it character by character.

Four Boolean variables are initially set to `False`:

```python
has_upper = False
has_lower = False
has_digit = False
has_special = False
```

The program then uses a loop to examine each character.

Depending on the character, the corresponding Boolean variable is changed to `True`.

After the character analysis is complete, the program checks the password length and creates suggestions for any missing requirements.

The number of requirements satisfied is then calculated and used to determine the password's strength.

---

## 7. Working Principle

The program follows these major steps:

### Step 1 — Accept Input

The user enters a password through the command line.

### Step 2 — Initialize Variables

The program initializes Boolean variables to track:

* Uppercase letters
* Lowercase letters
* Digits
* Special characters

### Step 3 — Analyze Characters

Each character of the password is examined using a loop.

The program identifies whether each character is:

* Uppercase
* Lowercase
* Numeric
* Special

### Step 4 — Check Password Length

The program checks whether the password contains at least eight characters.

### Step 5 — Generate Suggestions

If any requirement is missing, the program generates a corresponding suggestion.

### Step 6 — Calculate Strength

The program counts the number of requirements satisfied.

The classification is:

```text
0–2 checks passed → Weak
3–4 checks passed → Medium
5 checks passed   → Strong
```

### Step 7 — Display Result

The program displays the strength and, when necessary, suggestions for improvement.

---

## 8. Functional Requirements

The system should:

1. Accept a password as input.
2. Check the length of the password.
3. Detect uppercase letters.
4. Detect lowercase letters.
5. Detect numerical digits.
6. Detect special characters.
7. Count the requirements satisfied.
8. Classify the password as Weak, Medium, or Strong.
9. Display suggestions for missing requirements.
10. Inform the user that the program does not intentionally save the password.

---

## 9. Non-Functional Requirements

The program should:

* Be simple and easy to understand.
* Provide clear output.
* Execute quickly for normal password lengths.
* Require no external Python libraries.
* Be suitable for beginners learning Python.
* Avoid intentionally storing the entered password.

---

## 10. Input

The program accepts:

```text
Password entered by the user
```

Example:

```text
Hello123!
```

---

## 11. Output

The program displays:

* Password strength
* Suggestions, if any requirements are missing
* A note explaining that the program does not save the password

Example:

```text
Password strength: Strong
Your password meets all the checks in this program.
```

---

## 12. Algorithm

```text
START

Display "Password Strength Checker"

Input password

Set has_upper = False
Set has_lower = False
Set has_digit = False
Set has_special = False

FOR each character in password

    IF character is uppercase
        Set has_upper = True

    ELSE IF character is lowercase
        Set has_lower = True

    ELSE IF character is a digit
        Set has_digit = True

    ELSE
        Set has_special = True

END FOR

Create an empty suggestions list

IF password length < 8
    Add length suggestion

IF has_upper is False
    Add uppercase suggestion

IF has_lower is False
    Add lowercase suggestion

IF has_digit is False
    Add digit suggestion

IF has_special is False
    Add special-character suggestion

Count the number of requirements satisfied

IF checks passed <= 2
    Strength = Weak

ELSE IF checks passed <= 4
    Strength = Medium

ELSE
    Strength = Strong

Display strength

IF suggestions exist
    Display suggestions
ELSE
    Display success message

Display privacy note

STOP
```

---

## 13. Example Test Cases

| Input       | Expected Strength | Main Reason                                                       |
| ----------- | ----------------- | ----------------------------------------------------------------- |
| `hello`     | Weak              | Short and missing several character types                         |
| `Hello123`  | Medium            | Meets length, uppercase, lowercase and digit requirements         |
| `Hello123!` | Strong            | Meets all five requirements                                       |
| `12345678`  | Weak              | Only length and digit requirements are satisfied                  |
| `HELLO123`  | Medium            | Meets length, uppercase and digit requirements                    |
| `hello123!` | Medium            | Meets length, lowercase, digit and special-character requirements |

---

## 14. Limitations

Although the program provides a basic password-strength assessment, it does not perform a complete security analysis.

It does not consider:

* Whether a password appears in a known data breach.
* Whether the password is a commonly used password.
* Dictionary words.
* Personal information used in the password.
* Repeated patterns.
* Keyboard patterns.
* Password reuse.
* Password entropy.
* The estimated time required to guess the password.
* Modern password hashing or authentication systems.

Therefore, a password classified as "Strong" by this program is only strong according to the **five rules implemented in this project**.

---

## 15. Security Considerations

This project is an educational demonstration and should not be used as a production password-security system.

The program does not intentionally store the password in a file or database, and it does not print the password after input.

For real-world authentication systems, passwords should be handled using appropriate security practices such as secure password hashing, protected storage, rate limiting, and other application-specific security controls.

---

## 16. Complexity Analysis

Let `n` represent the length of the password.

The program examines every character once.

Therefore:

### Time Complexity

```text
O(n)
```

### Space Complexity

The program uses a fixed number of Boolean variables and a suggestions list with a fixed maximum number of entries.

Therefore, the additional space requirement is:

```text
O(1)
```

---

## 17. Expected Outcome

After completing this project, the user should be able to:

* Understand how strings can be processed character by character.
* Use loops for character analysis.
* Apply conditional statements to classify data.
* Use Boolean variables to track conditions.
* Create and use functions.
* Generate useful output based on user input.
* Understand basic algorithmic complexity.
* Recognize the difference between a basic educational checker and a complete security solution.

---

## 18. Future Enhancements

The project could be improved by implementing:

1. A graphical user interface.
2. A password generator.
3. Detection of common passwords.
4. Detection of repeated characters and patterns.
5. Entropy-based password analysis.
6. More detailed strength categories.
7. Unit testing.
8. Better handling of Unicode characters.
9. A configurable password policy.
10. Integration with secure password-management practices.

---

## 19. Conclusion

The Password Strength Checker demonstrates how fundamental Python programming concepts can be combined to create a small practical application.

By analyzing password length and character types, the program provides a simple classification and suggestions for improvement.

The project is primarily intended to strengthen understanding of **Python functions, loops, conditional statements, Boolean variables, lists, strings, and basic algorithmic complexity**.

It should be treated as an educational project rather than a complete password-security solution.
