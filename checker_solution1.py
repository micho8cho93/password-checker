#create a password strength checking program
#the program should check the password and then tell the user if it is weak, medium or strong

def checker():
    password = input("Enter your password: ")

    if len(password) < 6:
        print("Your passwords must be at least 6 characters long")
    elif len(password) > 6 and password.isalpha():
        print("Your password is weak")
    elif len(password) > 6 and password.isalnum():
        print("Your password is medium")
    elif len(password) > 6 and password.isalnum() and password.punctuation():
        print("Your password is strong")

checker()
#weak passwords only have characters

#medium passwords have characters and numbers

#strongs passwords have characters, numbers and special characters

