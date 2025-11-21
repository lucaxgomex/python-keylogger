from pynput.mouse import Controller
from pynput.keyboard import Controller

# Controlling the mouse
# Listening to the mousa

# Controlling the keyboard
# Listening to the keyboard - used at the keylogger
 
def control_mouse():
    mouse = Controller()
    mouse.move = (10, 20) # x, y

def control_keyboard():
    keyboard = Controller()
    keyboard.type("I am awesome")

