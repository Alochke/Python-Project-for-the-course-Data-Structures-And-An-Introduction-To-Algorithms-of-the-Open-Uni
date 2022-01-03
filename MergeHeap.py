"""
Stores the code for the MergeHeap class.
"""

import LinkedList


class MergeHeap(LinkedList.LinkedList):
    """
    A class representing a min-heap represented by a linked-list (utilizing the LinkedList class as a super.).
    Uses mode as a class variable to determine in which form out of three the terminal of the main function expects
    the data to be given as input:
    The value 1 is for sorted lists.
    The value 2 is for un-sorted lists.
    The value 3 is for un-sorted, disjointed lists.
    """
    mode = None

    def __init__(self, to_be_head):
        """Construct a MergeHeap and set up the self.head to to_be_head."""
        super().__init__(to_be_head)

    @classmethod
    def set_mode(cls, to_be_mode):
        """Set cls.mode to to_be_mode."""
        cls.mode = to_be_mode

    @classmethod
    # The function below Doesn't follow function-naming conventions to suite itself to the way __main__.main()'s
    # terminal commands are to be given as input.
    def MakeHeap(cls, list):
        """
        Turn list into mergeable-min-heap.
        """

        # The function relies on the value of cls.mode to determine the way it works to maximize efficiency.
        if cls.mode == 1:
            return cls(list.getHead())
        else:
            pass
