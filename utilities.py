"""All utility functions """

import os

#Clear the console to keep game neat
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
