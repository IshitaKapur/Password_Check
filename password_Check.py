def is_common_password(filename, password):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.strip() == password:
                return True
    return False

def main():
    while True:
        filename = input("Enter the path to the common password list file: ")
        try:
            # Test if file can be opened
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
        if is_common_password(filename, password):
            print("Warning: This password is common and not secure.")
        else:
            print("Good: This password is not in the common password list.")

if __name__ == "__main__":
    main()
