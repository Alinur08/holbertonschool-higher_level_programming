#!/usr/bin/python3
"""Module demonstrating multiple inheritance with Fish and Bird."""


class Fish:
    """Base class for aquatic animals."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Base class for avian animals."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Subclass inheriting from both Fish and Bird."""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
