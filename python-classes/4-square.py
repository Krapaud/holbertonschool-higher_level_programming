#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    __size = None

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du nouveau carré (par défaut 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré.

        Returns:
            int: La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré avec validation.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size * self.__size
