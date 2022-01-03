# The next class represents a Node of a linked-list, used primarily in the Linked-List class.

class Node:
    # A default-ive constructor for a Node object, setting up its value (val) and its following Node (next).
    def __init__(self, to_be_val, to_be_next):
        self.next = to_be_next
        self.val = to_be_val

    # A setter function for self's next node.
    def set_next(self, to_be_next):
        self.next = to_be_next

    # A setter function for self's value.
    def set_val(self, to_be_val):
        self.val = to_be_val

    # A getter function for self's next node.
    def get_next(self):
        return self.next

    # A getter function for self's value
    def get_val(self):
        return self.val
