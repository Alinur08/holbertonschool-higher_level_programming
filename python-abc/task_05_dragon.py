#!/usr/bin/python3
"""Module demonstrating the Mixin pattern in Python."""


class SwimMixin:
    """Provides swimming capability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Provides flying capability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that mixes in swimming and flying behaviors.
    """
    def roar(self):
        """Unique behavior for the Dragon class."""
        print("The dragon roars!")
