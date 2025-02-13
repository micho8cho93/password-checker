from getpass import getpass
import keyboard
import string

#must enter sudo python3 checker_solution2.py if admin access required
#might need to add python and python3 from venv to privacy and secuity -> accessibility
def strength(password):
    if len(password) < 6:
        print("Your passwords must be at least 6 characters long")
    elif len(password) > 6 and password.isalpha():
        print("Your password is weak")
    elif (len(password) > 6 and password.isalnum()) or (len(password) > 6 and string.punctuation(password)):
        print("Your password is medium")
    elif len(password) > 6 and password.isalnum() and string.punctuation(password):
        print("Your password is strong")

def checker():
    user = input("Enter your username: ")
    password = getpass("Enter your password: ")
    strength(password)

checker()