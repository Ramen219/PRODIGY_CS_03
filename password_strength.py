import re

def calculate_strenght(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[0-9]', password):
        score += 1

    if re.search(r'[\W_]', password):
        score += 1

    return score


def feedback(score):
    f = {
        0: "Very Weak",
        1: "Weak Password",
        2: "Moderate Passowrd",
        3: "Strong password",
        4: "Very Strong Password"
    }

    return f.get(score, "Invalid")


def main():
    password = input("Enter your Password: ")
    score = calculate_strenght(password)
    res = feedback(score)

    print(f"Password Strength: {res}")


if __name__ == "__main__":
    main()