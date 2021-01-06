from blessed import Terminal
from sys import stdout
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

current_position = (0, 0)


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
    global current_position
    current_position = (x, y)
    stdout.write(terminal.move_xy(x, y))


def move(x, y):
    global current_position
    current_position = (current_position[0] + x, current_position[1] + y)
    stdout.write(terminal.move_xy(current_position[0], current_position[1]))


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
while True:
    char = str(readchar.readchar(), "utf-8")
    if char == "w":
        move(0, 1)
    elif char == "a":
        move(-1, 0)
    elif char == "s":
        move(0, -1)
    elif char == "d":
        move(1, 0)
    stdout.write("#")
