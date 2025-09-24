#!/usr/bin/env python3
"""
Module pour l'exercice Dragon avec Mixins
"""


class SwimMixin:
    """Mixin pour la capacité de nager"""

    def swim(self):
        """Méthode pour nager"""
        print("The creature swims!")


class FlyMixin:
    """Mixin pour la capacité de voler"""

    def fly(self):
        """Méthode pour voler"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon héritant des mixins SwimMixin et FlyMixin"""

    def roar(self):
        """Méthode pour rugir"""
        print("The dragon roars!")

class draco(Dragon):
    def ability(self):
        print("fly():", self.fly())
        print("swim():", self.swim())
        print("habitat():", self.roar())

        print(draco.mro())


if __name__ == "__main__":
    flying_fish = draco()
    flying_fish.ability()
