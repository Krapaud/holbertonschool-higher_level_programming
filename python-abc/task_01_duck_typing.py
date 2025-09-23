#!/usr/bin/env python3
"""
Module pour l'exercice Duck Typing avec des formes géométriques
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe abstraite pour les formes géométriques"""

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire"""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre"""
        pass


class Circle(Shape):
    """Classe Circle héritant de Shape"""

    def __init__(self, radius):
        """Constructeur de Circle"""
        self.__radius = radius

    def area(self):
        """Calculer l'aire du cercle"""
        return math.pi * self.__radius**2

    def perimeter(self):
        """Calculer le périmètre du cercle"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Classe Rectangle héritant de Shape"""

    def __init__(self, width, height):
        """Constructeur de Rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculer l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculer le périmètre du rectangle"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Fonction qui utilise le duck typing pour afficher
    les infos d'une forme"""

    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
