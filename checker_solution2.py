from getpass import getpass
import keyboard

#must enter sudo python3 checker_solution2.py
#must add python and python3 from venv to privacy and secuity -> accessibility
def checker():
    user = input("Enter your username: ")
    password = getpass("Enter your password: ")
    while True:
        if keyboard.is_pressed('esc'):
                password = input()
        elif keyboard.is_pressed('enter'):
                password = input()

        if len(password) < 6:
            print("Your passwords must be at least 6 characters long")
        elif len(password) > 6 and password.isalpha():
            print("Your password is weak")
        elif len(password) > 6 and password.isalnum():
            print("Your password is medium")
        elif len(password) > 6 and password.isalnum() and password.punctuation():
            print("Your password is strong")

checker()