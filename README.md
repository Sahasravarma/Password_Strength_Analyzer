# Password Strength Analyzer

## Project Overview

Password Strength Analyzer is a Python-based mini project that evaluates
the strength of a password using multiple security checks.

The application analyzes password length, uppercase and lowercase letters,
numbers, special characters, repeated characters, predictable sequences,
common passwords, and character diversity.

It generates a security score from 0 to 10 and provides suggestions to
help users create stronger passwords.

## Features

- Password length analysis
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Repeated character detection
- Predictable sequence detection
- Common password detection
- Character diversity checking
- Security score from 0 to 10
- Password strength classification
- Suggestions for improving weak passwords
- Option to analyze multiple passwords
- Passwords are not stored

## Tech Stack

- Python 3
- Regular Expressions (re module)
- Lists
- Strings
- Conditional statements
- Loops
- Console-based input/output

## Setup

### 1. Clone the repository

git clone https://github.com/Sahasravarma/Password_Strength_Analyzer

### 2. Open the project folder

cd password-strength-analyzer

### 3. Run the program

python password_strength_analyzer.py

## Environment Variables

No environment variables are required for this project.

## API Notes

This project does not use any external APIs.

## Database Notes

This project does not use a database.
Passwords are analyzed locally and are not stored.

## How It Works

1. The user enters a password.
2. The program checks the password against multiple security rules.
3. A score from 0 to 10 is calculated.
4. The password is classified as Very Weak, Weak, Medium, Strong, or Very Strong.
5. Suggestions are displayed if security checks are not satisfied.
6. The user can analyze another password.

## Security Score

| Score | Strength |
|------:|----------|
| 9–10 | Very Strong |
| 7–8 | Strong |
| 5–6 | Medium |
| 3–4 | Weak |
| 0–2 | Very Weak |

## Team Member Contributions

### Sahasra
- Designed the Password Strength Analyzer concept.
- Developed the Python program.
- Implemented password security checks.
- Implemented the 0–10 scoring system.
- Implemented strength classification and suggestions.
- Tested the application and prepared project documentation.

## Project Status

Completed – Python Mini Project
