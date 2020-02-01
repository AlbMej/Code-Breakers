from blessed import Terminal
from ascii_art import *
import subprocess

class UserInterface:
    """
    A clean CLI for Code Breakers 
    """
    CIPHER_MSG = 'Test your Cipher Solutions'
    CIPHERCRACKER_MSG = 'Test your Cipher Cracker Solutions'
    COLORS = {"gold":"#ffd700",
              "pastel red":'#cc5454', 
              "moderate violet":"#673ab7",
              "bright red":'#f44336',}
    KEY_UP = 'KEY_UP'
    KEY_DOWN = 'KEY_DOWN'

    @classmethod
    def MainMenu(cls):
        """
        For Main Menu
        """
        t = Terminal()
        print(t.bold_white_on_red('Test your solutions against the Enigma machine!'), end ="")
        print(t.bold(" (Press 'q' to quit.)"))

        print(t.bold(f'    (1) {cls.CIPHER_MSG}'))
        print(t.bold(f'    (2) {cls.CIPHERCRACKER_MSG}'))

        user_input = input(t.bold("Enter 1 or 2: "))

        while True:
            if user_input == 'q':
                return
            elif user_input == '1':
                test = subprocess.Popen(["python3","testcipher.py"], stdout=subprocess.PIPE)
                user_input = input(t.bold("Enter 1 or 2: "))
                continue
            elif user_input == '2':
                test = subprocess.Popen(["python3","testciphercracker.py"], stdout=subprocess.PIPE)
                user_input = input(t.bold("Enter 1 or 2: "))
                continue
            else:
                print("Not a valid option")
                user_input = input(t.bold("Enter 1 or 2: "))


print(Terminal().bold_yellow(title()))
UserInterface.MainMenu()