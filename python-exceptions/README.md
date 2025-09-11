# Python - Exceptions

Ce projet fait partie du cursus Holberton School et se concentre sur la gestion des exceptions en Python. Il couvre les concepts fondamentaux de la gestion d'erreurs, les types d'exceptions, et les bonnes pratiques pour créer des programmes robustes.

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à quiconque, **sans l'aide de Google** :

### Concepts généraux

* Pourquoi la programmation Python est géniale
* Qu'est-ce qu'une exception et comment elle diffère d'une erreur
* Que sont les exceptions et comment les utiliser
* Quand utiliser les exceptions
* Comment gérer correctement une exception
* Quel est le but de capturer les exceptions
* Comment lever une exception intégrée
* Quand implémenter une fonction de nettoyage après une exception

## 📚 Concepts abordés

### Gestion des exceptions

* **try/except** : Capture et gestion des exceptions
* **try/except/else** : Exécution conditionnelle après try
* **try/except/finally** : Code de nettoyage obligatoire
* **raise** : Lever des exceptions personnalisées
* **assert** : Vérifications de débogage

### Types d'exceptions

* **Built-in exceptions** : ValueError, TypeError, IndexError, etc.
* **Custom exceptions** : Création d'exceptions personnalisées
* **Exception hierarchy** : Compréhension de la hiérarchie des exceptions

### Bonnes pratiques

* Gestion spécifique vs générale des exceptions
* Messages d'erreur informatifs
* Nettoyage des ressources
* Logging et debugging

## 📋 Prérequis

* Ubuntu 20.04 LTS ou distribution Linux compatible
* Python 3.8 ou supérieur
* Éditeur de texte ou IDE (VS Code, Vim, etc.)

## 🚀 Utilisation

1. **Cloner le repository** :

   ```bash
   git clone https://github.com/Krapaud/holbertonschool-higher_level_programming.git
   cd holbertonschool-higher_level_programming/python-exceptions
   ```

2. **Exécuter les scripts** :

   ```bash
   python3 script_name.py
   ```

3. **Tester avec des données spécifiques** :

   ```bash
   python3 main_file.py
   ```

## 📁 Structure du projet

```text
python-exceptions/
├── README.md                          # Ce fichier
├── 0-safe_print_list.py              # Impression sécurisée d'une liste
├── 0-main.py                         # Test pour 0-safe_print_list.py
├── 1-safe_print_integer.py           # Impression sécurisée d'un entier
├── 1-main.py                         # Test pour 1-safe_print_integer.py
├── 2-safe_print_list_integers.py     # Impression des entiers d'une liste
├── 2-main.py                         # Test pour 2-safe_print_list_integers.py
├── 3-safe_print_division.py          # Division sécurisée avec try/except/finally
├── 3-main.py                         # Test pour 3-safe_print_division.py
├── 4-list_division.py                # Division d'éléments de deux listes
├── 4-main.py                         # Test pour 4-list_division.py
├── 5-raise_exception.py              # Lever une exception TypeError
├── 5-main.py                         # Test pour 5-raise_exception.py
├── 6-raise_exception_msg.py          # Lever une exception avec message
├── 6-main.py                         # Test pour 6-raise_exception_msg.py
└── __pycache__/                      # Cache Python (généré automatiquement)
```

## 🔧 Fonctions principales

### Gestion sécurisée des opérations

* **safe_print_list(my_list=[], x=0)** : Imprime x éléments d'une liste de manière sécurisée
* **safe_print_integer(value)** : Imprime un entier avec gestion d'erreur, retourne True/False
* **safe_print_list_integers(my_list=[], x=0)** : Imprime les x premiers entiers d'une liste
* **safe_print_division(a, b)** : Effectue une division sécurisée avec try/except/finally
* **list_division(my_list_1, my_list_2, list_length)** : Divise élément par élément deux listes

### Manipulation des exceptions

* **raise_exception()** : Lève une exception TypeError
* **raise_exception_msg(message="")** : Lève une exception NameError avec message personnalisé

## 📝 Détails des tâches

### Task 0: Safe list printing

* **Fichier**: `0-safe_print_list.py`
* **Fonction**: `safe_print_list(my_list=[], x=0)`
* **Objectif**: Imprimer x éléments d'une liste de manière sécurisée
* **Gestion**: Capture les exceptions lors de l'accès aux éléments

### Task 1: Safe printing of an integers list

* **Fichier**: `1-safe_print_integer.py`
* **Fonction**: `safe_print_integer(value)`
* **Objectif**: Imprimer un entier avec le format "{:d}"
* **Retour**: True si l'impression réussit, False sinon

### Task 2: Print and count integers

* **Fichier**: `2-safe_print_list_integers.py`
* **Fonction**: `safe_print_list_integers(my_list=[], x=0)`
* **Objectif**: Imprimer les x premiers entiers d'une liste
* **Gestion**: Ignore les éléments non-entiers

### Task 3: Integers division with debug

* **Fichier**: `3-safe_print_division.py`
* **Fonction**: `safe_print_division(a, b)`
* **Objectif**: Division sécurisée avec affichage du résultat
* **Structure**: try/except/finally pour gérer la division par zéro

### Task 4: Divide a list

* **Fichier**: `4-list_division.py`
* **Fonction**: `list_division(my_list_1, my_list_2, list_length)`
* **Objectif**: Diviser élément par élément deux listes
* **Gestion**: Multiple exceptions (division par zéro, type, index)

### Task 5: Raise exception

* **Fichier**: `5-raise_exception.py`
* **Fonction**: `raise_exception()`
* **Objectif**: Lever une exception TypeError
* **Utilisation**: Démonstration de la levée d'exception

### Task 6: Raise a message

* **Fichier**: `6-raise_exception_msg.py`
* **Fonction**: `raise_exception_msg(message="")`
* **Objectif**: Lever une exception NameError avec message
* **Utilisation**: Exception personnalisée avec message

## 📖 Exemples d'utilisation

### Impression sécurisée d'une liste (Task 0)

```python
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
# Output: 12
#         nb_print: 2
```

### Impression sécurisée d'un entier (Task 1)

```python
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
print("has_been_print: {}".format(has_been_print))
# Output: 89
#         has_been_print: True
```

### Division sécurisée (Task 3)

```python
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("Inside result: {}".format(result))
# Output: 12 / 2 = 6.0
#         Inside result: 6.0
```

### Lever une exception (Task 5)

```python
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
# Output: Exception raised
```

## 🧪 Tests

Pour tester les fonctions, utilisez les fichiers main fournis :

```bash
# Test de la fonction safe_print_list
python3 0-main.py

# Test de la fonction safe_print_integer
python3 1-main.py

# Test de la fonction safe_print_list_integers
python3 2-main.py

# Test de la fonction safe_print_division
python3 3-main.py

# Test de la fonction list_division
python3 4-main.py

# Test de la fonction raise_exception
python3 5-main.py

# Test de la fonction raise_exception_msg
python3 6-main.py
```

### Exemple de test complet

```bash
# Exécuter tous les tests
for i in {0..6}; do
    echo "=== Test $i ==="
    python3 ${i}-main.py
    echo
done
```

## 🔍 Debugging

### Techniques recommandées

1. **Print statements** : Affichage des valeurs pour le débogage
2. **Try/except détaillé** : Capture d'exceptions spécifiques
3. **Logging** : Utilisation du module logging pour tracer les erreurs
4. **Assertions** : Vérifications de conditions avec assert

### Exemple de debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def divide_numbers(a, b):
    try:
        logging.debug(f"Attempting to divide {a} by {b}")
        result = a / b
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")
        return None
```

## 📝 Règles de codage

* Tous les fichiers doivent être exécutables
* Tous les fichiers doivent se terminer par une nouvelle ligne
* La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`
* Le code doit respecter le style PEP 8
* La longueur des fichiers sera testée avec `wc`
* Tous les modules doivent avoir une documentation
* Toutes les fonctions doivent avoir une documentation

## 🏆 Compétences développées

### Techniques

* Gestion robuste des erreurs
* Programmation défensive
* Debugging et troubleshooting
* Code maintenable et lisible

### Concepts avancés

* Hiérarchie des exceptions Python
* Context managers (with statement)
* Custom exception classes
* Exception chaining

## 🔗 Ressources utiles

* [Documentation officielle Python - Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [PEP 8 - Style Guide for Python Code](https://pep8.org/)
* [Real Python - Python Exceptions Handling](https://realpython.com/python-exceptions/)
* [W3Schools - Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

## 👨‍💻 Auteur

**Krapaud** - Étudiant à Holberton School France

## 📅 Historique des modifications

* **Septembre 2025** : Mise à jour complète du README avec détails des tâches
* **Correction Task 5** : Fix de la fonction `raise_exception()` pour lever une `TypeError`
* **Structure mise à jour** : Ajout des fichiers de test individuels

---

*Ce projet fait partie du cursus Holberton School et vise à développer des compétences solides en gestion d'exceptions et programmation défensive en Python.*
