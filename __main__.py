"""
This module is the main function of the program, which acts as a command terminal. For controlling,
changing, printing and creating mergeable heaps by command or by referring to the location of a txt-file of
commands.
Also, The module stores the functions which the main function utilizes but don't belong logically to a certain
class.
"""
from time import sleep
import MergeHeap
import os


def execute(command, txt_mode, wait, command_list, *args):
    """
    Execute the command given as parameter, while using:
    args - a tuple that contains all the created MergeHeaps, in chronological order from left to right,
    txt_mode - a boolean which indicates if reading commands from a command_list
    wait - a boolean that changes execution only when txt_mode == true and if true, shall wait between printing
    of the MergeHeaps, showing changes made by the commands given in chronological order.
    commands_list - irreverent when txt_mode == false, else wise, a list containing the commands left to be
    executed in chronological order, from left to right,

    """

    if command[0] == "I":
        # Insert was chosen.
        args[0].insert(int(command[7: len(command)]))

    if command == "Union":
        temp_list = list(args)
        temp_list[1].union(temp_list.pop())
        args = tuple(temp_list)

    if command == "FromTxt":
        print("Please type the path to the location of the txt file you wish to run commands from. \n"
              r"(for example:C:\Users\Alon\PycharmProjects\test.txt)")
        txt = open(input()).readlines()
        for i in range(len(txt)):
            txt[i] = txt[i][0: len(txt[i]) - 1]
        execute(txt.pop(), True, True, txt, *args)

    if command == "MakeHeap":
        temp_list = list(args)
        temp_list.append(MergeHeap.MergeHeap)
        args = tuple(temp_list)

    if command == "ExtractMin":
        args[0].extract_min()

    if command == "Minimum":
        print("The minimum is: " + args[0].get_head().get_val() + "/n")

    clear_console()
    print_iterable(args)

    if not txt_mode:
        guide_user()
        execute(input(), False, False, None, *args)

    if wait:
        sleep(5)
        # Nitay, I leave the skip related dialog and code here for you because you said you have a good idea
        # for implementation.

    execute(command_list.pop(), len(command_list) == 0, wait, command_list, *args)


def clear_console():
    """Clear the console."""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_iterable(iterable):
    """Print the given iterable object constructed of MergeHeaps."""
    for heap in iterable:
        heap.print_list()
        print("\n")
    print("\n")


def guide_user():
    """Encourage the user to give a command and show the formats of the commands."""
    print("Pleas chose one of the following commands: \n" +
          "MakeHeap, Insert [int], ExtractMin, Minimum, Union, FromTxt")


if __name__ == "__main__":
    print("Please decide in which form are you to input the data \n 1 - for sorted lists \n 2 - for un-sorted lists "
          "\n 3 - for un-sorted, disjointed lists.")
    MergeHeap.MergeHeap.set_mode(input())
    clear_console()
    guide_user()
    execute(input(), False, False, None)
