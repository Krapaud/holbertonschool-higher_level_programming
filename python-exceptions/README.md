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
├── README.md                    # Ce fichier
├── 0-safe_print_list.py        # Impression sécurisée d'une liste
├── 1-safe_print_integer.py     # Impression sécurisée d'un entier
├── 2-safe_print_list_integers.py # Impression des entiers d'une liste
├── 3-safe_print_division.py    # Division sécurisée
├── 4-list_division.py          # Division d'éléments de listes
├── 5-raise_exception.py        # Lever une exception de type
├── 6-raise_exception_msg.py    # Lever une exception avec message
└── main_files/                 # Fichiers de test
    ├── 0-main.py
    ├── 1-main.py
    └── ...
```

## 🔧 Fonctions principales

### Gestion sécurisée des opérations

* **safe_print_list()** : Imprime n éléments d'une liste de manière sécurisée
* **safe_print_integer()** : Imprime un entier avec gestion d'erreur
* **safe_print_division()** : Effectue une division avec gestion des erreurs

### Manipulation des exceptions

* **raise_exception()** : Exemple de levée d'exception de type
* **raise_exception_msg()** : Levée d'exception avec message personnalisé

## 📖 Exemples d'utilisation

### Gestion basique des exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Exceptions multiples

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Finally et nettoyage

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals():
        file.close()
```

## 🧪 Tests

Pour tester les fonctions, utilisez les fichiers main fournis :

```bash
# Test de la fonction safe_print_list
python3 0-main.py

# Test de la fonction safe_print_integer
python3 1-main.py

# Etc.
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

---

*Ce projet fait partie du cursus Holberton School et vise à développer des compétences solides en gestion d'exceptions et programmation défensive en Python.*
