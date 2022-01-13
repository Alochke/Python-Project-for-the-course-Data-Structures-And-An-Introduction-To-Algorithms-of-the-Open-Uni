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
        if MergeHeap.mode != 1:  # if mode = 1, all methods don't use these variables
            self.min = self.get_head().get_val() if to_be_head is not None else sys.maxsize  # holds the min value
        if MergeHeap.mode != 1:
            self.min = self.get_head().get_val() if to_be_head is not None else None
            if to_be_head is not None:
                self.tail = to_be_head  # initiating tail, points at the last node, only on mode 2 and 3
                if MergeHeap.mode == 2:
                    MergeHeap.values.append([self.head, self.head])  # updating values according to the mode format
                else:
                    MergeHeap.values.append([self.head])
            self.num_of_sub = 1  # hold the number of sub MergeHeaps uniting together.

    @classmethod
    def set_mode(cls, to_be_mode):
        """Set cls.mode to to_be_mode."""
        cls.mode = to_be_mode

    def insert(self, inserted):
        """Inserts inserted to self."""
        count = 0  # counter to find the right spot of the inserted value in the values array
        temp = self.head
        if MergeHeap.mode == 3:  # Binary searching if the value was already inserted to one of the MergeHeaps
            # if detecting the inserted number in the binary search, stop inserting
            i = 0
            while i < (len(MergeHeap.values) if self.get_head() is None else len(MergeHeap.values) - self.num_of_sub):
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
                i += 1
        if temp is None:
            # Self is empty, initiating head and tail
            self.head = Node.Node(inserted, None)
            if MergeHeap.mode != 1:
                self.tail = self.head
                if self.mode == 2:
                    MergeHeap.values.append([self.head, self.head])
                else:
                    MergeHeap.values.append([self.head])
                self.min = self.get_head().get_val()  # initiating min variable
        else:
            if temp.get_val() >= inserted:  # Inserted can be placed as head.
                self.head = Node.Node(inserted, temp)
                # correcting the values list for each mode
                if MergeHeap.mode == 3:
                    MergeHeap.values[len(MergeHeap.values) - self.num_of_sub] = \
                        [self.head] + MergeHeap.values[len(MergeHeap.values) - self.num_of_sub]
                if MergeHeap.mode == 2:
                    MergeHeap.values[len(MergeHeap.values) - self.num_of_sub][0] = self.head
                if MergeHeap.mode != 1 and self.min > self.head.get_val():
                    # New min detected, updating its self.min
                    self.min = self.head.get_val()
            else:
                if MergeHeap.mode == 1 or self.num_of_sub == 1:
                    while (temp.get_next() is not None) and (temp.get_next().get_val() < inserted):
                        # Searches correct insert position - keeping it sorted.
                        count += 1  # increasing the pointer of the inserted value in the values array (mode 3)
                        temp = temp.get_next()
                    node = Node.Node(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position (in the last two lines).
                    if MergeHeap.mode != 1:  # correcting values and tail for mode 2 and 3.
                        if node.get_next() is None: # new inserted node is the tail
                            self.tail = node
                            if self.mode == 2: # updating the tail in the values list for mode 2
                                MergeHeap.values[len(MergeHeap.values) - 1][1] = node
                        if self.mode == 3: # adding inserted node to the values list in mode 3
                            MergeHeap.values[len(MergeHeap.values) - self.num_of_sub][0: count + 1] += [node]

                else:
                    # Else, put inserted to a valid place in the first sub-heap.
                    end_node = MergeHeap.values[len(MergeHeap.values) - self.num_of_sub + 1][0]
                    while (temp.get_next() != end_node) and (temp.get_next().get_val() < inserted):
                        # Searches correct insert position - keeping it sorted.
                        count += 1  # increasing the pointer of the inserted value in the values array (mode 3)
                        temp = temp.get_next()
                    node = Node.Node(inserted, temp.get_next())
                    temp.set_next(node)  # Puts inserted to correct position.
                    # correcting values according to each mode and if needed
                    if MergeHeap.mode == 2 and node.get_next() == end_node:
                        MergeHeap.values[len(MergeHeap.values) - self.num_of_sub][1] = node
                    if MergeHeap.mode == 3:
                        self.values[len(self.values) - self.num_of_sub][0: count + 1] += [node]

    def union(self, merge_heap):
        """Unions self and merge_heap and saves the result in self."""
        if self.get_head() is None:  # Handling uniting empty MergeHeap with another.
            self.set_head(merge_heap.get_head())
            if MergeHeap.mode != 1:
                self.num_of_sub = merge_heap.num_of_sub
                if merge_heap.get_head is not None:  # If other mergeHeap is not empty, handle other self variables
                    self.min = merge_heap.min
                    self.tail = merge_heap.tail
            return
        if merge_heap.get_head() is not None:
            if MergeHeap.mode == 1:  # mode 1 detected - uniting both mergeheaps while sorting them
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
                    if j is None:  # Finished sorting and uniting
                        return
                while True:
                    # The loop goes through self and fits meregeheap's nodes in their place by order.
                    if (j.get_next() is None) or (i.get_next() is None):
                        if i.get_next() is not None:
                            # Making sure the nodes to right of i, will stay in self.
                            j.set_next(i.get_next())
                        i.set_next(j)
                        return
                    if j.get_val() < i.get_next().get_val():  # Found the correct place for j
                        temp = i.get_next()  # Save the next value of i to temp, so we can resign i.next.
                        i.set_next(j)
                        i = temp
                        while j.get_next() is not None and j.get_next().get_val() < temp.get_val():
                            # looping through j to find how many valid j nodes are in the right spot
                            j = j.get_next()
                        temp = j.get_next()  # saving current j.next to set j.next to be i
                        j.set_next(i)
                        if temp is None:  # finished sorting, return
                            return
                        j = temp
                    else:
                        i = i.get_next()
            else:  # union for mode 2 and 3
                self.tail.set_next(merge_heap.get_head())  # connecting one mergeheap's tail to other's head
                self.num_of_sub = self.num_of_sub + merge_heap.num_of_sub  # updating the number of sub heaps
                self.tail = merge_heap.tail  # updating the tail
                if self.min > merge_heap.min:  # updating the min value if needed
                    self.min = merge_heap.min

    def extract_min(self):
        """Extracts the minimal value's Node out of self."""
        if MergeHeap.mode == 1 or self.num_of_sub == 1:  # The minimum is simply the head
            self.head = self.head.get_next()  #
            if MergeHeap.mode != 1:  # updating the special variables for mode 2 and 3
                if self.get_head() is None:
                    self.min = self.get_head()
                    self.tail = None
                    MergeHeap.values.pop()
                else:
                    self.min = self.get_head().get_val()
                    # updating values for mode 2 and 3 according to each's unique format
                    if MergeHeap.mode == 2:
                        MergeHeap.values[len(MergeHeap.values) - 1][0] = self.get_head()
                    else:
                        # MergeHeap.Mode == 3, because MergeHeap.mode != 1.
                        MergeHeap.values[len(MergeHeap.values) - 1].pop(0)

        else:
            second_min = None  # holds the second minimum's node
            min = Node.Node(sys.maxsize, None)  # Initiating min to be maxSize, so the first node will replace him
            min_index = 0  # points the minimum value's index in the values array
            for i in range(len(MergeHeap.values) - self.num_of_sub, len(MergeHeap.values)):
                # looping through every first value in values sub lists and finding the minimum and second minimum
                # between them
                temp_min = MergeHeap.values[i][0]
                if temp_min.get_val() < min.get_val():  # new minimum detected
                    min = temp_min  # saving its node
                    min_index = i  # saving its location in values arr
                    # The long if statement bellow checks if temp_node.next.get_value()
                    # should be saved to second_min.
                    if min.get_next() is not None and \
                            (second_min is None or self.get_head().get_next().get_val() < second_min) \
                            and (len(MergeHeap.values) - 1 == min_index or
                                 min.get_next() != MergeHeap.values[min_index + 1][0]):
                        second_min = min.get_next().get_val()
                elif second_min is None or temp_min.get_val() < second_min:  # updating second min
                    second_min = temp_min.get_val()

            if self.get_head() == min:
                # min is the head of self, extracting it.
                self.head = self.head.get_next()
            else:
                # As long as min is not the head of self,
                # must append min.get_next() to the nodes to the left of min.
                self.values[min_index - 1][len(MergeHeap.values[min_index - 1]) - 1].set_next(min.get_next())

            if MergeHeap.mode == 2: # mode is 2, so values should be changed accordingly
                # checking if min node was the only item in its sub heap.
                if min.get_next() is not None and \
                        (len(MergeHeap.values) - 1 == min_index or
                         min.get_next() != MergeHeap.values[min_index + 1][0]):
                    MergeHeap.values[min_index][0] = min.get_next()
                else:
                    MergeHeap.values.pop(min_index)
                    self.num_of_sub -= 1
            else:
                MergeHeap.values[min_index].pop(0) #popping the min node.
                # checking if min node was the only item in its sub heap.
                if len(MergeHeap.values[min_index]) == 0:
                    MergeHeap.values.pop(min_index)
                    self.num_of_sub -= 1
            if len(MergeHeap.values) == min_index:
                self.tail = MergeHeap.values[min_index - 1][len(MergeHeap.values[min_index - 1]) - 1]
            self.min = second_min # updating self.min to be the second min

    def minimum(self):
        if MergeHeap.mode != 1:
            return self.min # returns the variable that holds minimum
        return self.head.get_val() # in mode 1 the head is the minimum (sorted linked list)
