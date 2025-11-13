import re

def password_strength(password: str) -> str:
    """
    Simple score-based password strength checker.
    Returns: "Very Weak", "Weak", "Medium", "Strong", ya "Very Strong"
    """

    score = 0
    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^\w\s]", password):
        score += 1

    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


if __name__ == "__main__":
    print("Simple Password Strength Checker\n")
    while True:
        pw = input("Enter your password (Or type 'exit' for quit): ")
        if pw.lower() == "exit":
            print("Bye!")
            break
        label = password_strength(pw)
        print(f"Strength: {label}\n")
