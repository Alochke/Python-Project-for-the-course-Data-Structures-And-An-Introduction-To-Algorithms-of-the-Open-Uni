import Node


class LinkedList:

    def __init__(self, to_be_head):
        self.head = Node.Node(to_be_head, None)

    def set_head(self, to_be_head):
        self.head = Node.Node(to_be_head, self.head)

    def get_head(self):
        return self.head