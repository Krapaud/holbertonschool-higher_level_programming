#!/usr/bin/python3
"""
Module pour la classe VerboseList qui étend la liste Python
"""


class VerboseList(list):
    """Classe qui étend list avec des notifications"""

    def append(self, item):
        """Ajouter un élément à la liste avec notification"""
        super().append(item)
        print("Add [{}] to the list.".format(item))

    def extend(self, items):
        """Étendre la liste avec notification"""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Supprimer un élément de la liste avec notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Supprimer et retourner un élément avec notification"""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
