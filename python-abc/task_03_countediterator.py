#!/usr/bin/python3
"""
Module pour la classe CountedIterator
"""


class CountedIterator:
    """Classe qui étend un itérateur en comptant les éléments parcourus"""

    def __init__(self, iterable):
        """Constructeur de CountedIterator"""
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        """Méthode pour obtenir le prochain élément"""
        try:
            item = next(self._iterator)
            self._count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Retourner le nombre d'éléments parcourus"""
        return self._count
