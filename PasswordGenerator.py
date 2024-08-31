import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 10:
        print("Password length should be at least 10 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("<--Welcome To Password Generator-->")
    length = int(input("Enter the desired length of the password (at least 10): "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()