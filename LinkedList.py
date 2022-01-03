import IntNode


# A class representing linked-lists.

class LinkedList:
    # A default-ive constructor, expecting an IntNode parameter to be set as self's head.
    def __init__(self, to_be_head):
        self.head = to_be_head

    # Returns true iff self is empty.
    def empty(self):
        return type(self.head) is None

    # A getter function for the head.
    def get_head(self):
        return self.head
