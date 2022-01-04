"""
This module is the main function of the program, which acts as a command terminal. For controlling,
changing, printing and creating mergeable heaps by command or by referring to the location of a txt-file of
commands.
Also, The module stores the functions which the main function utilizes but don't belong logically to a certain
class.
"""

import MergeHeap
import os
import sys
from colorama import *


def execute(command, *args):
    """
    Execute the command given as parameter, while using a tuple (args) that contains all the created MergeHeaps,
    in chronological order from left to right.
    """
    clear_console()

    if command == "FromTxt":
        pass

    if command == "MakeHeapFromList":
        pass

    print("Pleas chose one of the following commands: \n"
          "MakeHeap, MakeHeapFromList, Insert [int], ExtractMin, Minimum, Union, FromTxt")

    if command == "MakeHeap":
        execute(input(), *args, MergeHeap.MergeHeap(None))
    if command[0] == "I":
        pass
    if command == "ExtractMin":
        pass
    if command == "Minimum":
        pass
    # If none of the if statements above were entered then command == "Union".
    pass


def clear_console():
    """Clear the console."""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_pos(x, y, text_to_print):
    """Prints to (x,y) position the text given as parameter to cmd. Maybe useful in the future."""
    sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
    sys.stdout.flush()


if __name__ == "__main__":
    init()
    print("Please decide in which form are you to input the data \n 1 - for sorted lists \n 2 - for un-sorted lists "
          "\n 3 - for un-sorted, disjointed lists.")
    MergeHeap.MergeHeap.set_mode(input())
    clear_console()
    print("Pleas chose one of the following commands: \n"
          "MakeHeap, MakeHeapFromList, Insert [int], ExtractMin, Minimum, Union, FromTxt")
    execute(input())
