"""
Stores the code for the IntNode class.
"""


class IntNode:
    """
    Represents a Node of a linked-list, used in the LinkedList class.
    """

    def __init__(self, to_be_val, to_be_next):
        """Construct an IntNode and set self.next to to_be_next, self.val to to_be_val."""
        self.next = to_be_next
        self.val = to_be_val

    def set_next(self, to_be_next):
        """Set self.next to to_be_next."""
        self.next = to_be_next

    def set_val(self, to_be_val):
        """Set self.val to to_be_val."""
        self.val = to_be_val

    def get_next(self):
        """Return self.next."""
        return self.next

    def get_val(self):
        """Return self.val."""
        return self.val
