#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """Circle implementation of a Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle implementation of a Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Prints info about a shape using duck typing.
    """
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

if __name__ == "__main__":
    my_circle = Circle(5)
    my_rect = Rectangle(4, 10)

    print("--- Circle Info ---")
    shape_info(my_circle)

    print("\n--- Rectangle Info ---")
    shape_info(my_rect)
