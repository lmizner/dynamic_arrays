# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

from max_stack_da import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:

        # Push items on top of stack
        self.s1.push(value)


    def dequeue(self) -> object:

        if self.s1.size() == 0:
            raise QueueException

        # Pop items off of s1 stack and pushes them to s2 stack (temp)
        size = self.s1.size()

        for i in range(0, size-1):
            self.s2.push(self.s1.pop())

        print_value = self.s1.pop()

        # Add items back to s1 stack
        for i in range(0, self.s2.size()):
            self.s1.push(self.s2.pop())

        # Print value
        return print_value




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))
