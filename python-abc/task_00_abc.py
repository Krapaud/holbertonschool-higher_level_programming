#!/usr/bin/env python3
"""
Module defining an abstract Animal class and its subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Animal class that defines the interface for all animals
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        to return the sound that the animal makes
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal and implements the sound method
    """

    def sound(self):
        """
        Returns the sound that a dog makes

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal and implements the sound method
    """

    def sound(self):
        """
        Returns the sound that a cat makes

        Returns:
            str: "Meow"
        """
        return "Meow"
