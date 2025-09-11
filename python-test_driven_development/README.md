# Python - Test-driven development

Ce projet fait partie du cursus Holberton School et se concentre sur le développement piloté par les tests (TDD) en Python.

## 🎯 Objectifs d'apprentissage

* Qu'est-ce qu'un test interactif
* Pourquoi les tests sont importants
* Comment écrire des Docstrings pour créer des tests
* Comment écrire de la documentation pour chaque module et fonction
* Quelles sont les options de base pour créer des tests
* Comment trouver les cas limites

## 📁 Structure du projet

```text
python-test_driven_development/
├── README.md                          # Ce fichier
├── 0-add_integer.py                   # Addition de deux entiers
├── 0-main.py                          # Test pour 0-add_integer.py
├── 2-matrix_divided.py                # Division d'une matrice
├── 2-main.py                          # Test pour 2-matrix_divided.py
├── 3-say_my_name.py                   # Impression d'un nom
├── 3-main.py                          # Test pour 3-say_my_name.py
├── 4-print_square.py                  # Impression d'un carré
├── 4-main.py                          # Test pour 4-print_square.py
├── 5-text_indentation.py              # Indentation de texte
├── 5-main.py                          # Test pour 5-text_indentation.py
├── 6-max_integer.py                   # Trouver le maximum d'une liste
├── 6-main.py                          # Test pour 6-max_integer.py
└── tests/                             # Fichiers de test
    ├── 0-add_integer.txt              # Doctest pour 0-add_integer.py
    ├── 2-matrix_divided.txt           # Doctest pour 2-matrix_divided.py
    ├── 3-say_my_name.txt              # Doctest pour 3-say_my_name.py
    ├── 4-print_square.txt             # Doctest pour 4-print_square.py
    ├── 5-text_indentation.txt         # Doctest pour 5-text_indentation.py
    └── 6-max_integer_test.py          # Unittest pour 6-max_integer.py
```

## 🔧 Fonctions à implémenter

### Task 0: Integers addition
* **Fonction**: `add_integer(a, b=98)`
* **Fichier**: `0-add_integer.py`
* **Description**: Additionne deux entiers après conversion

### Task 1: Divide a matrix
* **Fonction**: `matrix_divided(matrix, div)`
* **Fichier**: `2-matrix_divided.py`
* **Description**: Divise tous les éléments d'une matrice

### Task 2: Say my name
* **Fonction**: `say_my_name(first_name, last_name="")`
* **Fichier**: `3-say_my_name.py`
* **Description**: Imprime "My name is <first name> <last name>"

### Task 3: Print square
* **Fonction**: `print_square(size)`
* **Fichier**: `4-print_square.py`
* **Description**: Imprime un carré avec le caractère #

### Task 4: Text indentation
* **Fonction**: `text_indentation(text)`
* **Fichier**: `5-text_indentation.py`
* **Description**: Formate un texte avec des indentations

### Task 5: Max integer - Unittest
* **Fonction**: `max_integer(list=[])`
* **Fichier**: `6-max_integer.py` (fourni)
* **Tests**: `tests/6-max_integer_test.py`
* **Description**: Tests unitaires pour la fonction max_integer

## 🧪 Exécution des tests

### Doctests
```bash
# Test d'une fonction spécifique
python3 -m doctest -v ./tests/0-add_integer.txt

# Test de tous les doctests
python3 -m doctest -v ./tests/*.txt
```

### Unittests
```bash
# Exécution des tests unitaires
python3 -m unittest tests.6-max_integer_test
```

### Tests avec les fichiers main
```bash
# Test des fonctions individuelles
./0-main.py
./2-main.py
./3-main.py
./4-main.py
./5-main.py
./6-main.py
```

## 📝 Instructions

1. **Toutes les fonctions sont à implémenter** - Les fichiers contiennent seulement les structures de base
2. **Les tests sont fournis** - Utilisez-les pour valider vos implémentations
3. **Respectez les prototypes** - Les signatures de fonctions ne doivent pas être modifiées
4. **Gestion des erreurs** - Implémentez toutes les exceptions requises

## 👨‍💻 Auteur

**Krapaud** - Étudiant à Holberton School France

---

*Ce projet fait partie du cursus Holberton School et vise à développer des compétences en test-driven development (TDD) en Python.*
