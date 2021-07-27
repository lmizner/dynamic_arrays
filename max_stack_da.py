# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:

        # Add element using the append function
        self.da_val.append(value)

        # Keep track of maximum value in stack
        size = self.da_max.length()

        if self.da_max.data.get(0) is None:
            self.da_max.append(value)
        elif value >= self.da_max.data.get(size-1):
            self.da_max.append(value)


    def pop(self) -> object:

        # Check if stack is empty
        if self.da_val.length == 0:
            raise StackException

        # Remove item from top of stack
        size = self.da_val.length()

        print_value = self.da_val.data.get(size-1)
        self.da_val.remove_at_index(size-1)

        # Remove value from MaxStack if maximum value
        max_size = self.da_max.length()

        if print_value == self.da_max.data.get(max_size-1):
            self.da_max.remove_at_index(max_size-1)

        # Print the value popped form the stack
        return print_value


    def top(self) -> object:

        # Check if stack is empty
        if self.da_val.size == 0:
            raise StackException

        # Determine value from top of stack
        size = self.size()
        print_value = self.da_val.data.get(size-1)

        # Print value from top of stack
        return print_value


    def get_max(self) -> object:

        # Check if stack is empty
        if self.da_max.length() == 0:
            raise StackException

        # Determine value from top of max stack
        size = self.da_max.length()
        print_value = self.da_max.data.get(size-1)

        # Print value from top of max stack
        return print_value



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
