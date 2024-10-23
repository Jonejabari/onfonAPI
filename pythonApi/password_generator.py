import random
import string

def generate_paasword(min_length, numbers=True, special_charecters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_charecters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_charecters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenght = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (Y/N)").lower() == "y"
has_special = input("Do you want to have special characters (Y/N)").lower() == "y"

pwd = generate_paasword(min_lenght, has_number, has_special)
print("The generated password is: ", pwd)