#This is my first project. All copyright reserved Ahmed Aribi aka _yxv_ 

#please read comments to understand the main ideas.
print(""" ____           ____   ____            
|  _ \__      _|  _ \ / ___| ___ _ __  
| |_) \ \ /\ / / | | | |  _ / _ \ '_ \ 
|  __/ \ V  V /| |_| | |_| |  __/ | | |
|_|     \_/\_/ |____/ \____|\___|_| |_|
                            by LPSB Team""")

import random
import string

def is_strong_password(password):
    # Define criteria for a strong password this should be changeable!
    length_check = len(password) >= 8
    digit_check = any(carac.isdigit() for carac in password)
    upper_check = any(carac.isupper() for carac in password)
    lower_check = any(carac.islower() for carac in password)
    symbol_check = any(carac in string.punctuation for carac in password)
    
    # Check
    return length_check and digit_check and upper_check and lower_check and symbol_check

def generate_password(name, age, length, easy_to_remember, full_with_symbols, specific_length):
    if easy_to_remember:
        # Ez to remember: include name, age, and random characters to fill the desired length
        password = f"{name}{age}"
        # The remaining length to fill
        remaining_length = length - len(password)
        # Add random characters
        password += ''.join(random.choices(string.ascii_letters + string.digits, k=remaining_length))
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        if full_with_symbols:
            characters = string.ascii_letters + string.digits + string.punctuation
        if specific_length:
            length = specific_length
        password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        print("\nChoose an option:")
        print("1. Check if inputted password is strong.")
        print("2. Generate a password.")
        print("3. Exit.")
        option = input("Enter your choice (1, 2, or 3): ")
        
        if option == '1':
            print(
        """A password is strong enough when it is at least 8 characters long and containing at least:
        1 Uppercase letter
        1 Lowercase letter
        1 Punctuation Symbol (/,#'...)
        1 Digit (0..9)""")
            
            password = input("Enter the password to check: ")
            if is_strong_password(password):
                print("The password is strong!")
            else:
                print("The password is not strong.")
        
        elif option == '2':
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            length = int(input("Enter the desired length of the password: "))
            easy_to_remember = input("Do you want the password to be easy to remember? (yes/no): ").lower() == 'yes'
            full_with_symbols = input("Do you want the password to be full of symbols? (yes/no): ").lower() == 'yes'
            specific_length = None
            if not easy_to_remember and not full_with_symbols:
                specific_length = length
            for i in range(4):
                password = generate_password(name, age, length, easy_to_remember, full_with_symbols, specific_length)
                print(str(i+1)+"th suggestion: ", password)
        
        elif option == '3':
            print("Exiting the program. Thank you for using our program!!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
