import LinkedList
import __main__


# A class representing a min-heap represented by a linked-list (utilizing the LinkedList class.).

class MergeHeap(LinkedList.LinkedList):
    # The variable below determines in which form out of three the terminal of the main function expects the
    # data to be given as input:
    # The value 1 is for sorted lists.
    # The value 2 is for un-sorted lists.
    # The value 3 is for un-sorted, disjointed lists.
    mode = None


    # A default-ive constructor, setting the head to to_be_head.
    def __init__(self, to_be_head):
        super().__init__(to_be_head)

    # A setter function for mode.
    @classmethod
    def set_mode(cls, to_be_mode):
        cls.mode = to_be_mode

    def insert(self, inserted):
        """Inserts inserted to self."""
        if MergeHeap.mode == 1:
            pass




    def union(self, merge_heap):
        """Unions self and merge_heap and saves the result in self."""
        pass

    def extract_min(self):
        """Extracts self.head without returning it while keeping self a mergeable heap by definition."""
        pass
