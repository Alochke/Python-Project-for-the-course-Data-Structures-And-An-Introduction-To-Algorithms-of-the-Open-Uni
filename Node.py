# The next class represents a Node of a linked-list, used primarily in the Linked-List class.

class Node:
    def __init__(self, to_be_val, to_be_next):
        self.next = to_be_next
        self.val = to_be_val

    def set_next(self, to_be_next):
        self.next = to_be_next

    def set_val(self, to_be_val):
        self.val = to_be_val

    def get_next(self):
        return self.next

    def get_val(self):
        return self.val
