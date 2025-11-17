# Python - Everything is object

## Description
Ce projet explore les concepts fondamentaux de Python concernant les objets, les références et la mémoire.

## Questions de compréhension

### What is an object?
**Qu'est-ce qu'un objet ?**

En Python, **tout est un objet**. Un objet est une entité qui contient :
- Des **données** (attributs/propriétés)
- Des **fonctions** (méthodes)
- Une **identité unique** (adresse mémoire donnée par `id()`)
- Un **type** (donné par `type()`)

Exemple : le nombre `42`, la chaîne `"Hello"`, une liste `[1, 2, 3]` sont tous des objets.

### What is the difference between a class and an object or instance?
**Quelle est la différence entre une classe et un objet ou une instance ?**

- **Classe** : C'est le "plan" ou le "modèle" qui définit la structure et le comportement
- **Objet/Instance** : C'est une réalisation concrète créée à partir d'une classe

Analogie : 
- Classe = Plan d'architecture d'une maison
- Objet = Maison réelle construite selon ce plan

```python
class Dog:  # Classe (le modèle)
    pass

rex = Dog()  # Instance/Objet (réalisation concrète)
max = Dog()  # Autre instance
```

### What is the difference between immutable object and mutable object?
**Quelle est la différence entre un objet immutable et mutable ?**

- **Immutable (Immutable)** : Un objet dont le contenu **ne peut PAS être modifié** après sa création. Toute "modification" crée un nouvel objet.
- **Mutable (Modifiable)** : Un objet dont le contenu **peut être modifié** sans créer un nouvel objet.

```python
# Immutable
s = "Hello"
s = s + " World"  # Crée une NOUVELLE chaîne

# Mutable
lst = [1, 2, 3]
lst.append(4)  # Modifie la MÊME liste
```

### What is a reference?
**Qu'est-ce qu'une référence ?**

Une **référence** est un "pointeur" vers un objet en mémoire. En Python, les variables ne contiennent pas directement les valeurs, mais des références vers les objets.

```python
a = [1, 2, 3]  # 'a' est une référence vers la liste [1, 2, 3]
```

### What is an assignment?
**Qu'est-ce qu'une assignation ?**

Une **assignation** (avec `=`) crée une référence d'une variable vers un objet. Elle ne copie pas l'objet, elle fait pointer la variable vers l'objet.

```python
a = [1, 2, 3]  # 'a' pointe vers [1, 2, 3]
b = a          # 'b' pointe vers le MÊME objet que 'a'
```

### What is an alias?
**Qu'est-ce qu'un alias ?**

Un **alias** est un autre nom (variable) qui pointe vers le même objet. Quand deux variables pointent vers le même objet, elles sont des alias l'une de l'autre.

```python
a = [1, 2, 3]
b = a          # 'b' est un alias de 'a'
b.append(4)
print(a)       # [1, 2, 3, 4] - 'a' est affecté car c'est le même objet
```

### How to know if two variables are identical?
**Comment savoir si deux variables sont identiques ?**

Utilise l'opérateur **`is`** pour vérifier si deux variables pointent vers le **même objet** (même identité/adresse mémoire).

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True - même objet
print(a is c)  # False - objets différents (même contenu)
```

### How to know if two variables are linked to the same object?
**Comment savoir si deux variables sont liées au même objet ?**

Utilise **`is`** ou compare leurs **`id()`** :

```python
a = [1, 2, 3]
b = a

# Méthode 1 : avec 'is'
print(a is b)  # True

# Méthode 2 : comparer les id
print(id(a) == id(b))  # True
```

### How to display the variable identifier (which is the memory address in the CPython implementation)?
**Comment afficher l'identifiant de variable (qui est l'adresse mémoire dans l'implémentation CPython) ?**

Utilise la fonction **`id()`** :

```python
a = 42
print(id(a))  # Affiche un nombre unique (ex: 140234567890)

b = 42
print(id(b))  # Peut être le même ID si Python optimise
```

### What is mutable and immutable?
**Qu'est-ce qui est mutable et immutable ?**

Voir la réponse détaillée dans "What is the difference between immutable object and mutable object" ci-dessus.

En résumé :
- **Immutable** : Ne peut pas être modifié (int, str, tuple)
- **Mutable** : Peut être modifié (list, dict, set)

### What are the built-in mutable types?
**Quels sont les types mutables intégrés ?**

Les types mutables principaux en Python :
- **`list`** - Liste : `[1, 2, 3]`
- **`dict`** - Dictionnaire : `{'key': 'value'}`
- **`set`** - Ensemble : `{1, 2, 3}`
- **`bytearray`** - Tableau d'octets modifiable

```python
my_list = [1, 2, 3]
my_list.append(4)  # ✓ Fonctionne - mutable

my_dict = {'a': 1}
my_dict['b'] = 2   # ✓ Fonctionne - mutable
```

### What are the built-in immutable types?
**Quels sont les types immutables intégrés ?**

Les types immutables principaux en Python :
- **`int`** - Entier : `42`
- **`float`** - Flottant : `3.14`
- **`bool`** - Booléen : `True`, `False`
- **`str`** - Chaîne de caractères : `"Hello"`
- **`tuple`** - Tuple : `(1, 2, 3)`
- **`frozenset`** - Ensemble immutable : `frozenset({1, 2, 3})`
- **`bytes`** - Séquence d'octets : `b"Hello"`
- **`NoneType`** - Type de `None`

```python
my_str = "Hello"
my_str[0] = "h"  # ✗ ERREUR - immutable

my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ✗ ERREUR - immutable
```

### How does Python pass variables to functions?
**Comment Python passe-t-il les variables aux fonctions ?**

Python utilise le **passage par référence** (ou plus précisément "passage par assignation" / "pass by object reference") :

- La **référence** de l'objet est passée à la fonction (pas une copie de l'objet)
- Pour les **immutables** : on ne peut pas modifier l'objet original (comportement similaire à "passage par valeur")
- Pour les **mutables** : on peut modifier le contenu de l'objet original

```python
# Avec un immutable (int)
def modify_int(n):
    n = n + 1  # Crée un NOUVEL objet local
    return n

a = 5
modify_int(a)
print(a)  # 5 - pas modifié

# Avec un mutable (list)
def modify_list(lst):
    lst.append(4)  # Modifie l'objet ORIGINAL

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] - modifié !

# Réassignation dans une fonction
def reassign_list(lst):
    lst = [99]  # Crée une NOUVELLE référence locale

my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list)  # [1, 2, 3] - pas modifié (réassignation locale)
```

**Règle importante** : 
- Si tu **modifies** le contenu d'un mutable → l'original est affecté
- Si tu **réassignes** la variable → l'original n'est PAS affecté

## Concepts clés à comprendre

### 1. Type et identité
- `type(obj)` : retourne le type d'un objet
- `id(obj)` : retourne l'identifiant unique (adresse mémoire) d'un objet

### 2. Comparaison : `==` vs `is`
- `==` : compare les **valeurs** des objets
- `is` : compare les **identités** (adresses mémoire) des objets

### 3. Objets mutables vs immutables

#### Immutables (ne peuvent pas être modifiés)
- `int`, `float`, `bool`
- `str` (chaînes de caractères)
- `tuple`

#### Mutables (peuvent être modifiés)
- `list`
- `dict`
- `set`

### 4. Optimisation de Python (interning)
Python optimise la mémoire en réutilisant certains objets :
- Petits entiers (-5 à 256)
- Chaînes courtes sans espaces
- Tuples vides

### 5. Passage par référence
En Python, tout est passé par référence :
- Les immutables se comportent comme "par valeur" (on ne peut pas les modifier)
- Les mutables peuvent être modifiés dans les fonctions

## Questions à te poser avant de répondre

Pour chaque exercice, demande-toi :
1. Quel est le type de l'objet ?
2. L'objet est-il mutable ou immutable ?
3. Est-ce que Python optimise cet objet ?
4. Est-ce une assignation directe ou une création de nouvel objet ?

## Comment tester tes réponses

Utilise l'interpréteur Python pour expérimenter :
```bash
python3
>>> a = 89
>>> b = 89
>>> id(a)
>>> id(b)
>>> a is b
```

## Ressources
- [Python Official Docs - Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python - Immutability in Python](https://realpython.com/immutable-python/)
- [Understanding Python's `is` vs `==`](https://realpython.com/python-is-identity-vs-equality/)

## Exercices

### Fichiers de réponses (`.txt`)
Contiennent une seule ligne avec la réponse :
- Nom de fonction (sans parenthèses)
- `Yes` ou `No`
- Résultat attendu

### Fichier Python (`19-copy_list.py`)
Fonction pour copier une liste (maximum 3 lignes)

## Astuce de débogage
Pour chaque question, teste le code dans l'interpréteur Python avant de répondre !
