
import keyboard

def on_key_event(e):
    if e.name == "a":  # Change this to the key you want to detect
        print("You pressed the 'A' key!")

keyboard.on_press(on_key_event)

print("Listening for key presses... Press 'esc' to exit.")
keyboard.wait("esc")  # Stop listening when 'esc' is pressed
