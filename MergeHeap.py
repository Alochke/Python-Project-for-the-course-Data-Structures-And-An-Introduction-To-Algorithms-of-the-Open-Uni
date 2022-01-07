"""
Stores the code for the MergeHeap class.
"""
import IntNode
import LinkedList
import math

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
        self.values = [[self.head.get_value()] if self.head is not None else []]
        #self.min = self.head.get_value() if self.head is not None else Integer.MIN_VALUE
        self.tail = to_be_head
        if MergeHeap.mode != 1:
            self.sub_heaps = []

    @classmethod
    def set_mode(cls, to_be_mode):
        """Set cls.mode to to_be_mode."""
        cls.mode = to_be_mode

    def insert(self, inserted):
        """Inserts inserted to self."""
        count = 0
        temp = self.head
        if MergeHeap.mode == 3:
            for arr in self.values:
                print(arr)
                low = 0
                high = len(arr) - 1
                while (low <= high):
                    mid = (high + low) // 2
                    if arr[mid] < inserted:
                        low = mid + 1
                    elif arr[mid] > inserted:
                        high = mid - 1
                    else:
                        return
        if temp is None:
            # Self is empty.
            self.head = IntNode.IntNode(inserted, None)
            self.tail = self.head
            self.values[0].append(inserted)
        else:
            if temp.get_val() >= inserted:
                # Self can be placed as head.
                self.head = IntNode.IntNode(inserted, temp)
                if MergeHeap.mode != 1 and self.sub_heaps != []:
                    self.sub_heaps[0] = self.head
            else:
                if MergeHeap.mode == 1 or self.sub_heaps == []:
                    while (temp.get_next() is not None) and (temp.get_next().get_val() < inserted):
                        # Searches correct insert position.
                        count += 1
                        temp = temp.get_next()
                    node = IntNode.IntNode(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position (in the last two lines).
                    if (node.get_next() is None) and MergeHeap.mode != 1:
                        self.tail = node
                else:
                    # Else, put inserted to a valid place in the first sub-heap.
                    end_node = self.sub_heaps[1]
                    while (temp.get_next() != end_node) and (temp.get_next().getval() < inserted):
                        # Searches correct place.
                        count += 1
                        temp = temp.get_next()
                    node = IntNode.IntNode(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position.
                    if temp == end_node:
                        self.sub_heaps[1] = node
                        self.tail = node
            self.values[0][0: count + 1] += [inserted] + [self.values[0][count + 1:]]


    def union(self, merge_heap):
        """Unions self and merge_heap and saves the result in self."""
        if self.get_head() is None:
            self.set_head(merge_heap.get_head())
            return
        if merge_heap.get_head() is not None:
            if MergeHeap.mode == 1:
                i = self.get_head()
                j = merge_heap.get_head()
                if j.get_val() < i.get_val():
                    # Adding the part of merge_heap which should come before the previous head of self.
                    self.head = merge_heap.get_head()
                    while (j.get_next() is not None) and (j.get_next().get_val() < i.get_val()):
                        j = j.get_next()
                    temp = j.get_next()  # Save the next value of j in temp, so we could set j.next to i.
                    j.set_next(i)
                    j = temp
                    if j is None:
                        return
                while True:
                    if (j.get_next() is None) or (i.get_next() is None):
                        if i.set_next is not None:
                            i = self.tail
                        i.set_next(j)
                        return
                    if j.get_val() < i.get_next.get_val():
                        temp = i.get_next()  # Save the next value of i to temp, so we can resign i.next.
                        i.set_next(j)
                        i = temp
                        while j.get_next is not None and j.get_next().getval() < temp.getval():
                            j = j.get_next()
                        temp = j.get_next()
                        j.set_next(i)
                        if temp is None:
                            return
                        j = temp
                    else:
                        i = i.get_next()
        else:
            if len(self.sub_heaps) == 0:
                self.sub_heaps.append(self.head)
                self.sub_heaps.append(self.tail)
            self.tail.set_next(merge_heap.get_head())
            self.sub_heaps.append(merge_heap.get_head())
            self.sub_heaps.append(merge_heap.tail)
            self.tail = merge_heap.tail
            # Last two lines can be problematic because of access rights, should be checked.

    def extract_min(self):
        """Extracts the minimal value's Node out of self."""
        if MergeHeap.mode == 1 or len(self.sub_heaps) == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.get_next()
        else:
            min = len(self.sub_heaps) - 1
            for i in range(int((len(self.sub_heaps) - 1) / 2)):
                if self.sub_heaps[i * 2].get_val() < self.sub_heaps[min].get_val():
                    min = i
            if self.sub_heaps[min] == self.get_head():
                # Correction, if needed, of self.get_head().
                self.set_head(self.get_head().get_next())
            if self.sub_heaps[min] == self.tail:
                # Correction, if needed, of self.tail.
                if len(self.sub_heaps) == 2:
                    self.tail = None
                else:
                    # Notice it can't be min = 0, because if it was, len(self.sub_heaps) == 2, because self's previous
                    # head is self's tail. So the line below is valid.
                    self.tail = self.sub_heaps[min - 1]
            if self.sub_heaps[min] == self.sub_heaps[min + 1]:
                # Correction, if needed, of self.sub_heaps (because the sub-heap of the minimum will be deleted.).
                self.sub_heaps.pop(min)
                self.sub_heaps.pop(min)
            else:
                # Correct the representation of the sub-heap of the minimum in self.sub_heap.
                self.sub_heaps[min] = self.sub_heaps[min].get_next()
            if min != 0:
                # As long as the extracted was not self's head, the actual list was not adjusted yet.
                self.sub_heaps[min - 1].set_next(self.sub_heaps[min])
