# pswd_Strength_Checker
This Python script evaluates the strength of a user-provided password based on specific criteria. It checks the password's length, complexity, and uniqueness relative to the user's username. The complexity assessment includes ensuring the presence of uppercase letters, lowercase letters, digits, and special characters. Based on these checks, the script categorizes the password strength as "weak," "moderate," "good," or "strong" and provides feedback to the user. The script can take input either interactively or through command-line arguments.

# Specifications of the Password Strength Checker Script

Language: Python3

__Functionality:__

* Length Check: Verifies that the password is at least 8 characters long.
* Complexity Check:
   * Contains at least one uppercase letter.
   * Contains at least one lowercase letter.
   * Contains at least one digit.
   * Contains at least one special character.
* Uniqueness Check: Ensures the password does not contain the username or parts of it.
* Strength Assessment: Categorizes password strength as "weak," "moderate," "good," or "strong."

**Input Methods:**

**Command Line:** Accepts password and username as command-line arguments.
Interactive Input: Prompts the user to enter the password and username interactively if no command-line arguments are provided.
Output:

**Provides feedback on the password strength.**
**Lists missing complexity criteria if the password is not strong.**

**Dependencies:**
Standard Python libraries (re, sys).

**Usage:**
Command Line: _python password_strength_checker.py "YourPassword123!" "YourUsername"_
Interactive: Run the script without arguments and enter the password and username when prompted.
