# Password Strength Checker 🔐

A simple Python-based **Password Strength Checker** that evaluates a password based on basic security requirements such as length, uppercase letters, lowercase letters, numbers, and special characters.

This project is designed as a beginner-friendly Python program to demonstrate the use of **functions, loops, conditional statements, strings, lists, Boolean variables, and user input**.

> **Note:** This is a basic classroom/learning project and is not a complete password-security or password-cracking analysis tool.

---

## 📌 Project Overview

The Password Strength Checker takes a password as input and checks whether it satisfies five basic requirements:

1. The password contains at least **8 characters**.
2. The password contains at least **one uppercase letter** (`A-Z`).
3. The password contains at least **one lowercase letter** (`a-z`).
4. The password contains at least **one digit** (`0-9`).
5. The password contains at least **one special character**, such as `!`, `@`, `#`, `$`, etc.

Based on how many of these requirements are satisfied, the program classifies the password as:

* **Weak**
* **Medium**
* **Strong**

If the password does not satisfy all requirements, the program also provides suggestions for improving it.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand how Python functions work.
* To practice using `for` loops.
* To work with strings and individual characters.
* To use conditional statements (`if`, `elif`, `else`).
* To understand Boolean variables.
* To use lists to store suggestions.
* To use Python string methods such as:

  * `isupper()`
  * `islower()`
  * `isdigit()`
* To understand how a program can evaluate multiple conditions.
* To provide meaningful feedback to the user.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Concepts Used:** Functions, loops, conditions, lists, strings, Boolean variables, user input
* **Interface:** Command-line / terminal

No external libraries are required.

---

## ⚙️ How the Program Works

The program is divided into two main functions:

### 1. `check_password(password)`

This function performs the actual password analysis.

It initially creates four Boolean variables:

```python
has_upper = False
has_lower = False
has_digit = False
has_special = False
```

These variables keep track of the different types of characters found in the password.

The program then examines every character using a `for` loop:

```python
for character in password:
```

Each character is checked using Python's built-in string methods.

### Uppercase Check

```python
if character.isupper():
    has_upper = True
```

If an uppercase character is found, `has_upper` becomes `True`.

### Lowercase Check

```python
elif character.islower():
    has_lower = True
```

If a lowercase character is found, `has_lower` becomes `True`.

### Number Check

```python
elif character.isdigit():
    has_digit = True
```

If a numerical digit is found, `has_digit` becomes `True`.

### Special Character Check

If a character is not an uppercase letter, lowercase letter, or digit, it is treated as a special character:

```python
else:
    has_special = True
```

---

## 📊 Password Requirements

The program checks five conditions:

| Requirement       | Condition                      |
| ----------------- | ------------------------------ |
| Minimum length    | At least 8 characters          |
| Uppercase         | At least one `A-Z`             |
| Lowercase         | At least one `a-z`             |
| Digit             | At least one `0-9`             |
| Special character | At least one special character |

Each condition that is satisfied contributes one point.

Therefore, the maximum score is **5**.

---

## 💪 Strength Classification

The program uses the following classification:

| Checks Passed | Strength |
| ------------: | -------- |
|           0–2 | Weak     |
|           3–4 | Medium   |
|             5 | Strong   |

The classification is implemented using:

```python
if checks_passed <= 2:
    strength = "Weak"
elif checks_passed <= 4:
    strength = "Medium"
else:
    strength = "Strong"
```

---

## 💡 Suggestions

If a password fails one or more requirements, the program provides suggestions.

For example, if there is no uppercase letter:

```text
Add at least one uppercase letter (A-Z).
```

If the password is shorter than eight characters:

```text
Use at least 8 characters.
```

If all requirements are satisfied, the program displays:

```text
Your password meets all the checks in this program.
```

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version using:

```bash
python3 --version
```

### Step 2: Save the Program

Save the Python code as:

```text
password_strength_checker.py
```

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python3 password_strength_checker.py
```

### Step 4: Enter a Password

The program will ask:

```text
Enter a password to check:
```

Enter the password you want to evaluate.

---

## 🖥️ Example Output

### Example 1 — Weak Password

```text
Password Strength Checker
-------------------------
Enter a password to check: hello

Password strength: Weak
Suggestions to improve it:
- Use at least 8 characters.
- Add at least one uppercase letter (A-Z).
- Add at least one number (0-9).
- Add at least one special character, such as ! or #.

Note: This program does not save your password.
```

### Example 2 — Medium Password

```text
Password Strength Checker
-------------------------
Enter a password to check: Hello123

Password strength: Medium
Suggestions to improve it:
- Add at least one special character, such as ! or #.

Note: This program does not save your password.
```

### Example 3 — Strong Password

```text
Password Strength Checker
-------------------------
Enter a password to check: Hello123!

Password strength: Strong
Your password meets all the checks in this program.

Note: This program does not save your password.
```

---

## 🔒 Privacy and Security Note

The program does **not intentionally save, store, or display the password after it has been entered**.

However, this project should still be considered an educational password checker rather than a professional security tool.

The program does not check for:

* Passwords found in data breaches
* Common or predictable passwords
* Repeated characters
* Keyboard patterns
* Password entropy
* Dictionary attacks
* Password reuse
* Cryptographic strength
* Estimated resistance to password guessing

For real applications, password security requires considerably more sophisticated techniques.

---

## ⏱️ Time Complexity

Let **n** be the number of characters in the password.

The program loops through the password once:

```python
for character in password:
```

Therefore, the character-checking portion takes:

**Time Complexity: O(n)**

The additional checks and suggestions operate on a constant number of conditions, so the overall time complexity remains:

**O(n)**

### Space Complexity

The program uses a small number of Boolean variables and a suggestions list.

The suggestions list can contain only a fixed number of messages based on the five checks.

Therefore, the additional space used is:

**O(1)**

---

## 📁 Project Structure

A simple project structure can be:

```text
Password-Strength-Checker/
│
├── password_strength_checker.py
├── README.md
└── STATEMENT.md
```

---

## 📚 Python Concepts Demonstrated

This project demonstrates several fundamental Python concepts:

### Functions

```python
def check_password(password):
```

Functions are used to organize the program into reusable sections.

### Lists

```python
suggestions = []
```

A list is used to store improvement suggestions.

### Loops

```python
for character in password:
```

The loop examines every character in the password.

### Conditional Statements

```python
if
elif
else
```

These are used to determine the type of each character and classify password strength.

### Boolean Variables

```python
has_upper = False
has_lower = False
```

Boolean values track whether each requirement has been satisfied.

### String Methods

The program uses:

```python
isupper()
islower()
isdigit()
```

to identify different types of characters.

---

## 🚀 Possible Future Improvements

The project can be extended by adding:

* Detection of commonly used passwords
* Detection of repeated characters
* Password entropy estimation
* A graphical user interface
* A password generator
* More detailed strength levels
* Checks against password dictionaries
* Better identification of special characters
* Unit tests
* Improved security practices for real-world applications

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

It provides a basic rule-based assessment and should not be considered a professional password-security auditing tool.

Users should avoid entering real, sensitive passwords into programs they do not trust.

---

## 👨‍💻 Project Type

**Beginner Python Project**

This project was created to practice fundamental programming concepts while building a small practical application.

---

## 📄 License

This project can be used, modified, and shared for educational purposes. If you publish a modified version, giving credit to the original project is appreciated.
