"""
Stores the code for the MergeHeap class.
"""
import IntNode
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
        """
        Create a new MergeHeap and if mode suggests doing so, add to the constructed the appropriate instance
        variables.
        """
        super().__init__(to_be_head)
        if MergeHeap.mode != 1:
            self.tail = to_be_head
            self.sub_heaps = []

    @classmethod
    def set_mode(cls, to_be_mode):
        """Set cls.mode to to_be_mode."""
        cls.mode = to_be_mode

    def insert(self, inserted):
        """Inserts inserted to self."""
        temp = self.head
        if temp is None:
            self.head = IntNode.IntNode(inserted, None)
        while (temp.get_next() is not None) and (not temp.get_next().getval() <= inserted):  # Searches correct
            # position for
            # inserted.
            temp = temp.get_next()
        temp.set_next(IntNode.IntNode(inserted, temp.get_next()))  # Puts inserted to correct position.

    def union(self, merge_heap):
        """Unions self and merge_heap and saves the result in self."""
        pass

    def extract_min(self):
        """Extracts self.head without returning it while keeping self a mergeable heap by definition."""
        self.head = self.head.get_next()
