from pynput.keyboard import Controller, Key
import time

# Create a keyboard controller
keyboard = Controller()

time.sleep(3)

# Function to type a string with special characters and uppercase letters
def type_special_characters():
    # Test special characters with explicit handling
    special_characters = {
        '@': [Key.shift, '2'],      # '@' requires Shift + 2
        '#': [Key.shift, '3'],      # '#' requires Shift + 3
        '$': [Key.shift, '4'],      # '$' requires Shift + 4
        '%': [Key.shift, '5'],      # '%' requires Shift + 5
        '^': [Key.shift, '6'],      # '^' requires Shift + 6
        '&': [Key.shift, '7'],      # '&' requires Shift + 7
        '*': [Key.shift, '8'],      # '*' requires Shift + 8
        '(': [Key.shift, '9'],      # '(' requires Shift + 9
        ')': [Key.shift, '0'],      # ')' requires Shift + 0
        '_': [Key.shift, '-'],      # '_' requires Shift + '-'
        '+': [Key.shift, '='],      # '+' requires Shift + '='
        '=': ['='],                 # '=' on standard QWERTY
        '{': [Key.shift, '['],      # '{' requires Shift + '['
        '}': [Key.shift, ']'],      # '}' requires Shift + ']'
        '[': ['['],                 # '['
        ']': [']'],                 # ']'
        ':': [Key.shift, ';'],      # ':' requires Shift + ';'
        ';': [';'],                 # ';'
        '"': [Key.shift, "'"],      # '"' requires Shift + "'"
        "'": ["'"],                 # "'"
        '<': [Key.shift, ','],      # '<' requires Shift + ','
        '>': [Key.shift, '.'],      # '>' requires Shift + '.'
        '.': ['.'],                 # '.'
        '?': [Key.shift, '/'],      # '?' requires Shift + '/'
        '/': ['/'],                 # '/'
        '\\': ['\\'],               # '\\'
        '|': [Key.shift, '\\']      # '|' requires Shift + '\\'
    }

    # Type each special character
    for char, keys in special_characters.items():
        # Press each key in the combination
        for key in keys:
            if isinstance(key, Key):  # Handle special keys like Shift
                keyboard.press(key)
            else:
                keyboard.press(key)  # Press the character key

        # Release each key in the combination
        for key in keys:
            if isinstance(key, Key):  # Handle special keys like Shift
                keyboard.release(key)
            else:
                keyboard.release(key)  # Release the character key

        time.sleep(0.5)  # Add delay between key presses

    # Type a newline at the end
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# Call the type_special_characters function to simulate typing
type_special_characters()