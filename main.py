import tkinter as tk
import random
import time
from pynput.keyboard import Controller, Key  # Import Key for special keys like backspace
import threading
from tkinter import messagebox

class TypingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Simulator")

        # UI Elements
        self.input_label = tk.Label(root, text="Enter text to simulate typing:")
        self.input_label.pack(pady=10)

        # Replacing Entry with Text widget for multi-line input
        self.input_field = tk.Text(root, width=50, height=5)
        self.input_field.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)

        self.keyboard_controller = Controller()  # pynput keyboard controller

    def random_typing_speed(self):
        # Random typing speed: simulate a range of speeds
        return random.uniform(0.05, 0.1)  # typing delay between 50ms to 100ms

    def random_typing_error(self):
        # Random typing error: simulate a mistake with a probability (e.g., 5%)
        return random.random() < 0.05  # 5% chance for a typing error

    def get_adjacent_key(self, char):
        # Get a random adjacent key from the layout
        nearby_keys = {
            'a': ['q', 'w', 's', 'z'],
            'b': ['v', 'g', 'h', 'n'],
            'c': ['x', 'v', 'f', 'd'],
            'd': ['e', 'r', 'f', 'c', 'x'],
            'e': ['w', 'r', 'd', 's', 'f'],
            'f': ['r', 't', 'g', 'd', 'v'],
            'g': ['t', 'y', 'h', 'f', 'b'],
            'h': ['y', 'u', 'j', 'g', 'n'],
            'i': ['u', 'o', 'k', 'j'],
            'j': ['u', 'i', 'k', 'h'],
            'k': ['i', 'o', 'l', 'j'],
            'l': ['o', 'p', 'k'],
            'm': ['n', 'j', 'k'],
            'n': ['b', 'm', 'j', 'h'],
            'o': ['i', 'p', 'l'],
            'p': ['o', 'l'],
            'q': ['w', 'a'],
            'r': ['e', 'd', 'f', 't'],
            's': ['a', 'w', 'd', 'x'],
            't': ['r', 'f', 'g', 'y'],
            'u': ['y', 'i', 'j'],
            'v': ['c', 'b', 'g'],
            'w': ['q', 'e', 's', 'a'],
            'x': ['z', 's', 'd', 'c'],
            'y': ['t', 'h', 'u', 'g'],
            'z': ['a', 'x'],
            '0': ['9', '8'],
            '1': ['2', 'q'],
            '2': ['1', '3', 'w'],
            '3': ['2', '4', 'e'],
            '4': ['3', '5', 'r'],
            '5': ['4', '6', 't'],
            '6': ['5', '7', 'y'],
            '7': ['6', '8', 'u'],
            '8': ['7', '9', 'i'],
            '9': ['8', '0', 'o'],
        }
        if char in nearby_keys:
            return random.choice(nearby_keys[char])
        return char  # If no adjacent keys, return the original char

    def type_special_character(self, char):
        # Handle individual special characters
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

        # Retrieve the key combination for the special character
        keys = special_characters.get(char)
        if keys:
            # Press each key in the combination
            for key in keys:
                if isinstance(key, Key):  # Handle special keys like Shift
                    self.keyboard_controller.press(key)
                else:
                    self.keyboard_controller.press(key)  # Press the character key

            # Release each key in the combination
            for key in keys:
                if isinstance(key, Key):  # Handle special keys like Shift
                    self.keyboard_controller.release(key)
                else:
                    self.keyboard_controller.release(key)  # Release the character key

            time.sleep(0.5)  # Add delay between key presses

    def type_text(self, text):
        start_time = time.time()  # Record the start time of the typing simulation

        time.sleep(1)  # 1-second delay before typing starts

        for i in range(len(text)):
            char = text[i]
            # Check if there should be a typing error
            if self.random_typing_error():
                # Simulate an error by typing an adjacent wrong character
                wrong_char = self.get_adjacent_key(char)
                self.keyboard_controller.press(wrong_char)  # Type the wrong character
                self.keyboard_controller.release(wrong_char)
                time.sleep(self.random_typing_speed())
                # Simulate pressing backspace to erase the wrong character
                self.keyboard_controller.press(Key.backspace)  # Corrected backspace key
                self.keyboard_controller.release(Key.backspace)
                time.sleep(self.random_typing_speed())

            # Handle special characters
            if char in "!@#$%^&*()_+{}[]|:;<>,.?/~":
                self.type_special_character(char)
            else:
                # Handle uppercase characters
                if char.isupper():
                    self.keyboard_controller.press(Key.shift)  # Hold Shift for uppercase
                    self.keyboard_controller.press(char.lower())  # Type lowercase character but with Shift for uppercase
                    self.keyboard_controller.release(char.lower())
                    self.keyboard_controller.release(Key.shift)
                else:
                    # Type the correct character
                    self.keyboard_controller.press(char)  # Press the key
                    self.keyboard_controller.release(char)  # Release the key
                time.sleep(self.random_typing_speed())  # Wait for a short random period between keystrokes

            if char == " ":
                time.sleep(random.uniform(0.1, 0.3))  # Short pause after each word

            if char == "." or char == "?":
                time.sleep(random.uniform(0.3, 0.8))  # Longer pause after each sentence

            if char == "\n":  # For line breaks, simulate pressing the Enter key
                self.keyboard_controller.press(Key.enter)  # Corrected Enter key handling
                self.keyboard_controller.release(Key.enter)
                time.sleep(self.random_typing_speed())  # Ensure only one line break is inserted

        end_time = time.time()  # Record the end time of the typing simulation
        total_time = round(end_time - start_time, 2)  # Calculate the total typing time

        # After typing is complete, show the alert with the total typing time
        self.show_alert(total_time)

    def show_alert(self, total_time):
        # Show an alert with the total typing time
        messagebox.showinfo("Typing Finished", f"Typing simulation has been completed!\nTotal Time: {total_time} seconds")

    def start_typing(self):
        text = self.input_field.get("1.0", tk.END).strip()  # Get text input from user (for Text widget)

        # Start typing in the currently focused window (e.g., Notepad)
        typing_thread = threading.Thread(target=self.type_text, args=(text,))
        typing_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    typing_simulator = TypingSimulator(root)
    root.mainloop()
