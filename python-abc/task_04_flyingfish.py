#!/usr/bin/env python3
"""
Module pour l'exercice FlyingFish avec héritage multiple
"""


class Fish:
    """Classe Fish avec méthodes swim et habitat"""

    def swim(self):
        """Méthode pour nager"""
        print("The fish lives in water")

    def habitat(self):
        """Méthode pour l'habitat"""
        print("The bird lives in the sky")


class Bird:
    """Classe Bird avec méthodes fly et habitat"""

    def fly(self):
        """Méthode pour voler"""
        print("The bird is flying")

    def habitat(self):
        """Méthode pour l'habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Classe FlyingFish héritant de Fish et Bird"""

    def fly(self):
        """Méthode fly surchargée"""
        print("The flying fish is soaring!")

    def swim(self):
        """Méthode swim surchargée"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Méthode habitat surchargée"""
        print("The flying fish lives both in water and the sky!")

    def test_flyingfish(self):
        """Test et explore le MRO du FlyingFish"""
        print("fly():", self.fly())
        print("swim():", self.swim())
        print("habitat():", self.habitat())

        print(FlyingFish.mro())


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.test_flyingfish()
