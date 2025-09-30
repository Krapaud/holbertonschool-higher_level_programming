# Python - Input/Output

Ce projet fait partie du cursus Holberton School et se concentre sur la manipulation des entrées et sorties en Python. Il couvre la lecture et l'écriture de fichiers, la sérialisation et la désérialisation JSON, ainsi que la gestion des arguments de la ligne de commande.

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à quiconque, **sans l'aide de Google** :

### Concepts généraux

- Pourquoi la programmation Python est géniale
- Comment ouvrir un fichier
- Comment écrire du texte dans un fichier
- Comment lire le contenu complet d'un fichier
- Comment lire un fichier ligne par ligne
- Comment déplacer le curseur dans un fichier
- Comment s'assurer qu'un fichier est fermé après son utilisation
- Qu'est-ce que l'instruction `with` et comment l'utiliser
- Qu'est-ce que le JSON
- Qu'est-ce que la sérialisation
- Qu'est-ce que la désérialisation
- Comment convertir une structure de données Python en chaîne JSON
- Comment convertir une chaîne JSON en structure de données Python
- Comment accéder aux paramètres de la ligne de commande dans un script Python

## 📚 Concepts abordés

### Gestion de fichiers

- **`open()`** : Ouverture de fichiers avec différents modes (`r`, `w`, `a`, `r+`, etc.)
- **`read()`**, **`readline()`**, **`readlines()`** : Lecture de contenu
- **`write()`** : Écriture de chaînes de caractères
- **`close()`** : Fermeture explicite des fichiers
- **`with open(...) as ...`** : Gestionnaire de contexte pour la fermeture automatique
- **`seek()`**, **`tell()`** : Manipulation du curseur

### Sérialisation JSON

- **`json.dump()`** & **`json.dumps()`** : Sérialisation d'objets Python en JSON
- **`json.load()`** & **`json.loads()`** : Désérialisation de JSON en objets Python

### Ligne de commande

- **`sys.argv`** : Accès aux arguments passés à un script

## 📋 Prérequis

- Ubuntu 20.04 LTS ou distribution Linux compatible
- Python 3.8.5 ou supérieur
- Éditeur de texte ou IDE (VS Code, Vim, etc.)
- Style de code `pycodestyle` (version 2.7.*)

## 🚀 Utilisation

1.  **Cloner le repository** :

    ```bash
    git clone https://github.com/Krapaud/holbertonschool-higher_level_programming.git
    cd holbertonschool-higher_level_programming/python-input_output
    ```

2.  **Exécuter les scripts** :

    ```bash
    python3 <nom_du_script.py>
    ```

## 📝 Règles de codage

- **Éditeurs autorisés** : `vi`, `vim`, `emacs`
- **Interprétation** : Tous les fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS avec `python3` (version 3.8.5)
- **Fin de fichier** : Tous les fichiers doivent se terminer par une nouvelle ligne
- **Shebang** : La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`
- **README** : Un fichier `README.md` à la racine du dossier du projet est obligatoire
- **Style de code** : Le code doit respecter `pycodestyle` (version 2.7.*)
- **Exécutable** : Tous les fichiers doivent être exécutables
- **Longueur des fichiers** : La longueur des fichiers sera testée avec `wc`

## 🧪 Tests

- Placez tous les fichiers de test dans le dossier `tests`
- Les fichiers de test doivent être au format texte (`.txt`)
- Pour exécuter les tests, utilisez la commande : `python3 -m doctest ./tests/*`
- Ajoutez une documentation à chaque module, classe et fonction

## 📂 Exercices du projet

Ce projet contient plusieurs exercices pratiques couvrant les concepts d'entrées/sorties :

- **Lecture et écriture de fichiers** - Manipulation basique des fichiers
- **Sérialisation JSON** - Conversion d'objets Python en JSON et vice versa
- **Arguments de ligne de commande** - Traitement des paramètres sys.argv
- **Triangle de Pascal** - Algorithme mathématique avec structures de données

## 🏆 Compétences développées

- Manipulation des fichiers texte
- Sérialisation et désérialisation de données avec JSON
- Interaction avec le système via les arguments de la ligne de commande
- Programmation robuste et gestion des ressources
- Implémentation d'algorithmes mathématiques

## 📞 Contact

**Auteur** : Krapaud - Étudiant Holberton School

## 📄 Licence

Ce projet est réalisé dans le cadre du cursus **Holberton School** à des fins éducatives uniquement.

### Conditions d'utilisation

- ✅ **Consultation** : Libre consultation du code à des fins d'apprentissage
- ✅ **Inspiration** : Utilisation comme référence pour comprendre les concepts
- ❌ **Copie directe** : Interdiction de copier le code pour des projets académiques
- ❌ **Distribution commerciale** : Aucune utilisation commerciale autorisée

### Clause éducative

Ce repository contient des solutions d'exercices pédagogiques. Il est destiné à :
- Partager des connaissances avec la communauté d'apprentissage
- Démontrer la maîtrise des concepts enseignés
- Servir de référence pour d'autres étudiants

**Note importante** : Si vous êtes étudiant, utilisez ce code pour comprendre les concepts, mais développez vos propres solutions pour respecter l'intégrité académique.

---
*Ce projet fait partie du cursus Holberton School et vise à développer des compétences solides en gestion des entrées/sorties en Python.*