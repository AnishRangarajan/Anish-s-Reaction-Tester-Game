import board
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.A0, board.A1, board.A2, board.A3, board.D5]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.F5,       # Num Lock (start / stop game)
        KC.SPACE,    # 7
        KC.SPACE,    # 8
        KC.SPACE,    # 4
        KC.SPACE,    # 5
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()