import MergeHeap
import os


# This module is the main function of the program, which acts as a command terminal. For controlling,
# changing, printing and creating mergeable heaps by command or by referring to the location of a txt-file of
# commands.

# Definition of the main function to make use of recursion.
def main():
    print("Please decide in which form are you to input the data \n 1 - for sorted lists \n 2 - for un-sorted lists "
          "\n 3 - for un-sorted, disjointed lists.")
    MergeHeap.MergeHeap.set_mode(input())
    clear_console()
    print("...")


# A function which clears the console.
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# The command below initiates the program.
if __name__ == "__main__":
    main()
