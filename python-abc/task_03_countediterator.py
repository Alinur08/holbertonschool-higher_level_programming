#!/usr/bin/python3
"""Module defining an iterator that tracks its own progress."""


class CountedIterator:
    """An iterator wrapper that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.
        """
        self.__iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Returns the current number of items that have been iterated."""
        return self.__count

    def __next__(self):
        """
        Fetches the next item and increments the counter.
        """
        item = next(self.__iterator)
        self.__count += 1
        return item

    def __iter__(self):
        """Ensures the class itself is an iterator (standard Python practice)."""
        return self
