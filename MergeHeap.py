"""
Stores the code for the MergeHeap class.
"""
import Node
import LinkedList
import sys


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
    values = []

    def __init__(self, to_be_head):
        """
        Create a new MergeHeap and if mode suggests doing so, add to the constructed the appropriate instance
        variables.
        """

        super().__init__(to_be_head)
        if MergeHeap.mode != 1:
            self.min = self.get_head().get_val() if to_be_head is not None else sys.maxsize
            self.tail = to_be_head
            if to_be_head is not None:
                self.tail = self.head
                MergeHeap.values.append([self.head])
            self.num_of_sub = 1

    @classmethod
    def set_mode(cls, to_be_mode):
        """Set cls.mode to to_be_mode."""
        cls.mode = to_be_mode

    def insert(self, inserted):
        """Inserts inserted to self."""
        count = 0
        temp = self.head
        if MergeHeap.mode == 3:
            i = 0
            while i < len(MergeHeap.values) - self.num_of_sub + 1:
                low = 0
                high = len(MergeHeap.values[i]) - 1
                while low <= high:
                    mid = (high + low) // 2
                    if MergeHeap.values[i][mid].get_val() < inserted:
                        low = mid + 1
                    elif MergeHeap.values[i][mid].get_val() > inserted:
                        high = mid - 1
                    else:
                        return
                i = i + 1
        if temp is None:
            # Self is empty.
            self.head = Node.Node(inserted, None)
            if MergeHeap.mode != 1:
                self.tail = self.head
                MergeHeap.values.append([self.head])
                self.min = self.get_head().get_val()
        else:
            if temp.get_val() >= inserted:
                # Inserted can be placed as head.
                self.head = Node.Node(inserted, temp)
                if MergeHeap.mode == 3:
                    MergeHeap.values[len(MergeHeap.values) - self.num_of_sub] = \
                        [self.head] + MergeHeap.values[len(MergeHeap.values) - self.num_of_sub]
                if MergeHeap.mode == 2:
                    MergeHeap.values[len(MergeHeap.values) - self.num_of_sub] = [self.head]
                if MergeHeap.mode != 1 and self.min > self.head.get_val():
                    self.min = self.head.get_val()
            else:
                if MergeHeap.mode == 1 or self.num_of_sub == 1:
                    while (temp.get_next() is not None) and (temp.get_next().get_val() < inserted):
                        # Searches correct insert position.
                        count += 1
                        temp = temp.get_next()
                    node = Node.Node(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position (in the last two lines)
                    if node.get_next() is None:
                        self.tail = node
                    if MergeHeap.mode == 3:
                        self.values[len(self.values) - self.num_of_sub][0: count + 1] += [node]
                else:
                    # Else, put inserted to a valid place in the first sub-heap.
                    end_node = MergeHeap.values[len(MergeHeap.values) - self.num_of_sub + 1][0]
                    while (temp.get_next() != end_node) and (temp.get_next().getval() < inserted):
                        # Searches correct place.
                        count += 1
                        temp = temp.get_next()
                    node = Node.Node(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position.
                    if MergeHeap.mode == 3:
                        self.values[len(self.values) - self.num_of_sub][0: count + 1] += [node]

    def union(self, merge_heap):
        """Unions self and merge_heap and saves the result in self."""
        if self.get_head() is None:
            self.set_head(merge_heap.get_head())
            if MergeHeap.mode != 1:
                self.num_of_sub = merge_heap.num_of_sub
                if merge_heap.get_head is not None:
                    self.min = merge_heap.min
                    self.tail = merge_heap.tail
            return
        if merge_heap.get_head() is not None:
            if MergeHeap.mode == 1:
                i = self.get_head()
                j = merge_heap.get_head()
                if j.get_val() < i.get_val():
                    # Adding the part of merge_heap which should come before the previous head of self.
                    self.head = merge_heap.get_head()
                    self.min = merge_heap.get_head().get_val()
                    while (j.get_next() is not None) and (j.get_next().get_val() < i.get_val()):
                        j = j.get_next()
                    temp = j.get_next()  # Save the next value of j in temp, so we could set j.next to i.
                    j.set_next(i)
                    j = temp
                    if j is None:
                        return
                while True:
                    # The loop goes through self and fits merege_heap's nodes in their place by order.
                    if (j.get_next() is None) or (i.get_next() is None):
                        if i.get_next() is not None:
                            # Making sure the nodes to right of i, will stay in self.
                            j.set_next(i.get_next())
                        i.set_next(j)
                        return
                    if j.get_val() < i.get_next().get_val():
                        temp = i.get_next()  # Save the next value of i to temp, so we can resign i.next.
                        i.set_next(j)
                        i = temp
                        while j.get_next() is not None and j.get_next().get_val() < temp.get_val():
                            j = j.get_next()
                        temp = j.get_next()
                        j.set_next(i)
                        if temp is None:
                            return
                        j = temp
                    else:
                        i = i.get_next()
            else:
                self.tail.set_next(merge_heap.get_head())
                self.num_of_sub = self.num_of_sub + merge_heap.num_of_sub
                self.tail = merge_heap.tail
                if self.min > merge_heap.min:
                    self.min = merge_heap.min

    def extract_min(self):
        """Extracts the minimal value's Node out of self."""
        if MergeHeap.mode == 1 or self.num_of_sub == 1:
            if self.head == self.tail:
                self.tail = None
            MergeHeap.values[0].pop(0)
            if len(MergeHeap.values[0]) == 0:
                MergeHeap.values.pop(0)
            self.head = self.head.get_next()
        else:
            min = Node.Node(sys.maxsize, None)
            for i in range(len(MergeHeap.values) - self.num_of_sub, len(MergeHeap.values)):
                temp_min = MergeHeap[i][0]
                second_min = MergeHeap[i][0]
                if temp_min.get_val() < min.get_val():
                    min = temp_min
                    temp_index = i
                    second_min = temp_min

            MergeHeap.values[temp_index].pop(0)
            if temp_index == len(MergeHeap.values) - self.num_of_sub:
                self.head = self.head.get_next()

            if len(MergeHeap.values[i]) == 0:
                MergeHeap.values.pop(i)
                self.num_of_sub -= 1
                if temp_index == len(MergeHeap.values) - 1:
                    self.tail = MergeHeap.values[i - 1][len(MergeHeap.values[i - 1])]

            self.min = second_min
            return min



