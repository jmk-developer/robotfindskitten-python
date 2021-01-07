from blessed import Terminal
from sys import stdout, exit
from time import sleep
import readchar
import random
import os

terminal = Terminal()

vanilla_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "texts", "vanilla")
vanilla_file = open(vanilla_path, "r")
vanilla_text = vanilla_file.read()
vanilla_file.close()
vanilla = vanilla_text.split("\n")

board_items = []
board_size = (32, 32)
board_colors = [

]


def vanilla_pick():
    return random.choice(vanilla)


def clear():
    stdout.write(terminal.clear)


def home():
    stdout.write(terminal.home)


def reset():
    clear()
    home()


def goto(x, y):
    stdout.write(terminal.move_xy(x, y))


def move(x, y):
    current_position = terminal.get_location()
    goto(current_position[1] + x, current_position[0] - y)


reset()
stdout.write("""robotfindskitten v1
By the illustrious Leonard Richardson (C) 1997, 2000
Written originally for the Nerth Pork robotfindskitten contest
Adapted for Python by jmkdev, Jan 6 2021

In this game, you are robot (#). Your job is to find kitten. This task
is complicated by the existence of various things which are not kitten.
Robot must touch items to determine if they are kitten or not. The game
ends when robotfindskitten.

Press any key to start.
""")

readchar.readchar()
reset()
stdout.write("robotfindskitten v1")
stdout.write("\n\n")
stdout.write("─" * board_size[0])
stdout.write("\n")

while True:
    char = str(readchar.readchar(), "utf8")

    final_move = [0, 0]
    if char == "w":
        final_move[1] += 1
    if char == "a":
        final_move[0] -= 1
    if char == "s":
        final_move[1] -= 1
    if char == "d":
        final_move[0] += 1
    if char == "x":
        break

    move(final_move[0], final_move[1])
    stdout.write("#")
    move(-1, 0)

reset()
exit()
