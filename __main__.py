"""
This module is the main function of the program, which acts as a command terminal. For controlling,
changing, printing and creating mergeable heaps by command or by referring to the location of a txt-file of
commands.
Also, The module stores the functions which the main function utilizes but don't belong logically to a certain
class.
"""
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
    executed in chronological order, from left to right.

    """

    if command[:1] == "I":
        # Insert was chosen, inserting the value chosen to the last Mergeheap in the args
        args[len(args) - 1].insert(int(command[7:]))

    if command == "Union":
        # uniting last 2 MergeHeaps in the args
        temp_list = list(args)
        temp_list[len(temp_list) - 2].union(temp_list.pop())
        args = tuple(temp_list)

    if command == "FromTxt":
        print("Please type the path to the location of the txt file you wish to run commands from, "
              "without the .txt ending. \n" + r"(for example:C:\Users\Alon\PycharmProjects\commands)")
        with open(input()) as file:
            # opening the path chosen
            txt = file.readlines()
            for i in range(len(txt) - 1):
                # Last line is saved to txt priorly to the loop without "/n"
                txt[i] = txt[i][0: len(txt[i]) - 1]
            txt.reverse()
            # executing each line in the text file
            execute(txt.pop(), True, True, txt, *args)

    if command == "MakeHeap":
        # adding the new empty heap to the args list
        temp_list = list(args)
        temp_list.append(MergeHeap.MergeHeap(None))
        args = tuple(temp_list)

    if command == "ExtractMin":
        # extracting the minimum value from the MergeHeap handled at the moment.
        args[len(args) - 1].extract_min()

    clear_console()
    print_iterable(args)
    print("")

    if command == "Minimum":
        # printing the minimum value
        print("The minimum is: " + str(args[len(args) - 1].minimum()) + "\n")

    if not txt_mode:
        # text mode is False, so continuing to ask for commands input
        guide_user()
        execute(input(), False, False, None, *args)

    if wait:
        print('To skip to the end-result type "skip", for the next step press enter:')
        wait = (input() != "skip")

    execute(command_list.pop(), len(command_list) != 0, wait, command_list, *args)


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


def guide_user():
    """Encourage the user to give a command and show the formats of the commands."""
    print("Pleas chose one of the following commands: \n" +
          "MakeHeap, Insert [int], ExtractMin, Minimum, Union, FromTxt")


if __name__ == "__main__":
    # starting the main
    print("Please decide in which form are you to use the program: \n 1 - for sorted lists \n 2 - for un-sorted lists "
          "\n 3 - for un-sorted, disjointed lists.")
    MergeHeap.MergeHeap.set_mode(int(input()))
    clear_console()
    guide_user()
    execute(input(), False, False, None)
