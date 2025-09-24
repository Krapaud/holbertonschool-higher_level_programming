#!/usr/bin/python3
"""
Module pour l'exercice Dragon avec Mixins.
Démontre l'utilisation des mixins pour ajouter des capacités à une classe.
"""


class SwimMixin:
    """Mixin qui ajoute la capacité de nager à une classe."""

    def swim(self):
        """Fait nager la créature."""
        print("The creature swims!")


class FlyMixin:
    """Mixin qui ajoute la capacité de voler à une classe."""

    def fly(self):
        """Fait voler la créature."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon qui hérite des capacités de nage et de vol via les mixins.

    Hérite de SwimMixin et FlyMixin pour obtenir les capacités swim() et fly().
    """

    def roar(self):
        """Fait rugir le dragon."""
        print("The dragon roars!")


class draco(Dragon):
    """Classe draco héritant de Dragon pour tester les capacités et le MRO."""

    def ability(self):
        """Teste toutes les capacités du dragon et affiche le MRO."""
        print("fly():", self.fly())
        print("swim():", self.swim())
        print("roar():", self.roar())

        print(draco.mro())


if __name__ == "__main__":
    new_draco = draco()
    new_draco.ability()
