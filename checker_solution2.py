from getpass import getpass
import string

def punctuation(password):
    for i in password:
        if i in string.punctuation:
            return True
    return False

def numbers(password):
    for i in password:
        if i in string.digits:
            return True
    return False

def letters(password):
    for i in password:
        if i in string.ascii_letters:
            return True
    return False



def checker():
    user = input("Enter your username: ")
    if letters(user) == True or numbers(user) == True or punctuation(user) == True:
        print('If you want to hide your password, enter X. If you want to see your password, enter S')

    choice = input("Your choice (X/S): ").strip().lower()
        
    if choice == "x":
        print("\nPassword will be hidden")
        password = getpass("Enter your password: ")
    elif choice == "s":
        print("\nPassword will be visible")
        password = input("Enter your password: ")
    else:
        print("Invalid choice. Please enter 'X' or 'S'.")

    if len(password) < 6:
        print("Your passwords must be at least 6 characters long")
    elif len(password) > 6 and letters(password) and numbers(password) == False and punctuation(password) == False:
        print("Your password is weak")
    elif len(password) > 6 and letters(password) and numbers(password) == True and punctuation(password) == False:
        print("Your password is medium strength")
    elif len(password) > 6 and letters(password) and numbers(password) == True and punctuation(password) == True:
        print("Your password is strong")
    return

checker()
