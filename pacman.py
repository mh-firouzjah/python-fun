import sys
import tkinter as tk
from tkinter.constants import END

from colorama import Back, Fore, Style

WALL = f"{Back.BLACK}{Fore.WHITE}#{Style.RESET_ALL}"
POINT = f'{Back.BLACK}{Fore.LIGHTYELLOW_EX}.{Style.RESET_ALL}'

BOX_DRAWING_CHARS = {
    "middle_single": (u'\u253C', '┼'),
    "left_top_single": (u'\u250c', '┌'),
    "right_top_single": (u'\u2510', '┐'),
    "top_middle_single": (u'\u252C', '┬'),
    "horizontal_single": (u'\u2500', '─'),
    "left_middle_single": (u'\u251C', '├'),
    "left_bottom_single": (u'\u2514', '└'),
    "right_middle_single": (u'\u2524', '┤'),
    "right_bottom_single": (u'\u2518', '┘'),
    "bottom_middle_single": (u'\u2534', '┴'),
    "vertical_pipe_single": (u'\u2502', '│'),
    "middle_doubled": (u'\u256C', '╬'),
    "left_top_doubled": (u'\u2554', '╔'),
    "right_top_doubled": (u'\u2557', '╗'),
    "top_middle_doubled": (u'\u2566', '╦'),
    "horizontal_doubled": (u'\u2550', '═'),
    "left_bottom_doubled": (u'\u255a', '╚'),
    "left_middle_doubled": (u'\u2560', '╠'),
    "right_middle_doubled": (u'\u2563', '╣'),
    "right_bottom_doubled": (u'\u255d', '╝'),
    "bottom_middle_doubled": (u'\u2569', '╩'),
    "vertical_pipe_doubled": (u'\u2551', '║'),
}


def rpl(self):
    for value in BOX_DRAWING_CHARS.values():
        WALL = f"{Back.BLACK}{Fore.WHITE}{value[1]}{Style.RESET_ALL}"
        self = self.replace(value[1], WALL)
    return self.replace('.', POINT)


screen = [
    rpl('╔══╦═══╦════════╦═══╦══╗'),
    rpl('║..║   ║........║   ║..║'),
    rpl('║..╚═══╝.╔════╗.╚═══╝..║'),
    rpl('║........║    ║........║'),
    rpl('╠═╗.╔══╗.╚════╝.╔══╗.╔═╣'),
    rpl('║ ║.║  ║........║  ║.║ ║'),
    rpl('║ ║.║  ║.╔═..═╗.║  ║.║ ║'),
    rpl('╠═╝.╚══╝.║....║.╚══╝.╚═╣'),
    rpl('║........║....║........║'),
    rpl('╠═╗.╔══╗.╚════╝.╔══╗.╔═╣'),
    rpl('║ ║.║  ║........║  ║.║ ║'),
    rpl('║ ║.╚══╝.╔════╗.╚══╝.║ ║'),
    rpl('║ ║......║    ║......║ ║'),
    rpl('║ ║.╔══╗.║    ║.╔══╗.║ ║'),
    rpl('╠═╝.║  ║.╚════╝.║  ║.╚═╣'),
    rpl('║...╚══╝........╚══╝...║'),
    rpl('╠═╗......╔════╗......╔═╣'),
    rpl('║ ║......║    ║......║ ║'),
    rpl('╚═╩══════╩════╩══════╩═╝'),
]

# window = tk.Tk()
# window.resizable(False, False)

# scr = tk.Text(window)
# for row in screen:
#     scr.insert(END, row + '\n')
# scr.pack()

# window.mainloop()


def print_tablet():
    print()
    for row in screen:
        sys.stdout.flush()
        print(row)
    print()


print_tablet()
