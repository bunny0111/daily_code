# Password Strength Checker
import re

'''
Conditions:
    password strength check conditions:
        minimum 8 characters, min 1 digit, min 1 uppercase alphabet, lowercase, and special character
'''

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters"

    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain a digit"

    if not any(char.isupper() for char in password):
        return "Weak: Password must contain an upper character"

    if not any(char.islower() for char in password):
        return "Weak: Password must contain a lower character"

    if not re.search(r'[!@#$%^&*(){}<>.?]', password):
        return "Medium: Password must contain a special character"
    
    return "Strong: Your password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)
        print(result)

# Run the password checker tool
if __name__ == "__main__":
    password_checker()

'''
Use of if __name__ == "__main__": in Python
The if __name__ == "__main__": construct is used in Python scripts to ensure that certain code is only executed when the script is run directl
'''