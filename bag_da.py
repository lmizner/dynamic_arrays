# Course: CS261 - Data Structures
# Student Name: Lauren Mizner
# Assignment: Assignment 2
# Description:

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:

        # Add element using the append function
        self.da.append(value)


    def remove(self, value: object) -> bool:

        # Check each index and if equal to value,
        # then apply remove_at_index function
        for i in range(0, self.size()):
            if self.da.data[i] == value:
                self.da.remove_at_index(i)
                return True

        # Otherwise, return false if nothing is removed
        return False


    def count(self, value: object) -> int:

        # Initialize count value
        count_value = 0

        # Cycle through bag to count number of value occurrences
        for i in range(0, self.da.size):
            if self.da.data[i] == value:
                count_value += 1

        # Return final count total
        return count_value


    def clear(self) -> None:

        # Update dynamic array variables to clear previous data
        self.da.data = None
        self.da.capacity = 0
        self.da.size = 0


    def equal(self, second_bag: object) -> bool:

        # Check for different size arrays
        if self.size() != second_bag.size():
            return False

        length = self.size()

        # Check for empty array
        if length == 0:
            return True

        # Set new dynamic arrays
        new_array_1 = DynamicArray()
        new_array_2 = DynamicArray()
        size = self.da.size

        # Create new changeable arrays
        for i in range(0, size):
            new_array_1.append(self.da.data.get(i))
            new_array_2.append(second_bag.da.data.get(i))

        def sa_sort(arr: StaticArray, size) -> None:

            # Implement an insertion sort to be used in equal function
            for index in range(1, size):
                value = arr.get(index)
                pos = index - 1

                while pos >= 0 and arr.get(pos) > value:
                    arr.set(pos + 1, arr.get(pos))
                    pos -= 1
                    arr.set(pos + 1, value)

        # Use insertion sort function
        sa_sort(new_array_1.data, length)
        sa_sort(new_array_2.data, length)

        for i in range(0, size):
            if new_array_1.data.get(i) != new_array_2.data.get(i):
                return False

        return True


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
