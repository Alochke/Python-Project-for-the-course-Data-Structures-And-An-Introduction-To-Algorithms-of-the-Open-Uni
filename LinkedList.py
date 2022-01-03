"""
Stores the code for the LinkedList class.
"""


class LinkedList:
    """
    A class representing linked-lists.
    """

    def __init__(self, to_be_head):
        """Construct a LinkedList and set self.head to to_be_head."""
        self.head = to_be_head

    def empty(self):
        """Return true iff self is empty."""
        return type(self.head) is None

    def get_head(self):
        """Return self.head."""
        return self.head
