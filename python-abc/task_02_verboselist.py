#!/usr/bin/python3
"""Module defining a list that notifies on every modification."""


class VerboseList(list):
    """A list subclass that prints messages when modified."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list and prints the count of items added."""
        items_to_add = list(iterable)
        count = len(items_to_add)
        super().extend(items_to_add)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Prints notification before removing a specific item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item by index."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
