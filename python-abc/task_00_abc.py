#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract Base Class for Animals.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """Must be implemented by all subclasses."""
        pass

class Dog(Animal):
    """Subclass representing a Dog."""
    
    def sound(self):
        """Implementation of the abstract sound method."""
        return "Bark"

class Cat(Animal):
    """Subclass representing a Cat."""
    
    def sound(self):
        """Implementation of the abstract sound method."""
        return "Meow"
