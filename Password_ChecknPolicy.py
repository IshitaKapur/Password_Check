import re

def is_common_password(filename, password):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.strip() == password:
                return True
    return False

def check_password_policy(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, "Password meets the policy requirements."

def main():
    while True:
        filename = input("Enter the path to the common password list file: ")
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore'):
                pass
            break
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please try again.")

    print("Type 'exit' to quit.")
    while True:
        password = input("Enter a password to check: ")
        if password.lower() == 'exit':
            break

        policy_ok, policy_msg = check_password_policy(password)
        if not policy_ok:
            print(f"Policy violation: {policy_msg}")
            continue

        if is_common_password(filename, password):
            print("Warning: This password is common and not secure.")
        else:
            print("Good: This password is not in the common password list and meets the policy.")

if __name__ == "__main__":
    main()
