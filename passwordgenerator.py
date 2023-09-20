import random
import string
def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    complexity = ""
    while not complexity:
        print("Select complexity level:")
        print("1. Easy (only lowercase letters)")
        print("2. Medium (lowercase + uppercase letters)")
        print("3. Strong (lowercase + uppercase + digits)")
        print("4. Ultra Strong (lowercase + uppercase + digits + special characters)")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            complexity = lowercase_letters
        elif choice == '2':
            complexity = lowercase_letters + uppercase_letters
        elif choice == '3':
            complexity = lowercase_letters + uppercase_letters + digits
        elif choice == '4':
            complexity = lowercase_letters + uppercase_letters + digits + special_characters
        else:
            print("Invalid choice. Please select a valid option.")
    password = ''.join(random.choice(complexity) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Invalid length. Please enter a positive number.")
        return
    password = generate_password(length)
    print("Generated Password: " + password)
if __name__ == "__main__":
    main()