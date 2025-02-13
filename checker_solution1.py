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
    password = input("Enter your password: ")

    if len(password) < 6:
        print("Your passwords must be at least 6 characters long")
    elif len(password) > 6 and letters(password) and numbers(password) == False and punctuation(password) == False:
        print("Your password is weak")
    elif len(password) > 6 and letters(password) and numbers(password) == True and punctuation(password) == False:
        print("Your password is medium")
    elif len(password) > 6 and letters(password) and numbers(password) == True and punctuation(password) == True:
        print("Your password is strong")
        
    return

checker()
