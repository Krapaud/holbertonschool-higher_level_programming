# SQL - Introduction

Ce projet contient une série de scripts SQL pour apprendre les bases de MySQL et manipuler des bases de données.

## Description

Ce projet fait partie du cursus Holberton School et couvre les concepts fondamentaux de SQL, notamment :
- La création et la suppression de bases de données
- La création et la manipulation de tables
- Les requêtes SELECT avec filtres et tri
- Les opérations INSERT, UPDATE et DELETE
- Les fonctions d'agrégation (COUNT, AVG)
- Le regroupement de données (GROUP BY)

## Environnement

- **OS** : Ubuntu 20.04 LTS
- **MySQL** : Version 8.0
- **Shell** : bash

## Fichiers

### 0. List databases
**Fichier** : `0-list_databases.sql`

Script qui liste toutes les bases de données disponibles sur le serveur MySQL.

**Commande utilisée** : `SHOW DATABASES;`

**Exemple d'utilisation** :
```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

---

### 1. Create a database
**Fichier** : `1-create_database_if_missing.sql`

Script qui crée la base de données `hbtn_0c_0` si elle n'existe pas déjà.

**Commande utilisée** : `CREATE DATABASE IF NOT EXISTS`

**Exemple d'utilisation** :
```bash
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

---

### 2. Delete a database
**Fichier** : `2-remove_database.sql`

Script qui supprime la base de données `hbtn_0c_0` si elle existe.

**Commande utilisée** : `DROP DATABASE IF EXISTS`

**Exemple d'utilisation** :
```bash
cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
```

---

### 3. List tables
**Fichier** : `3-list_tables.sql`

Script qui liste toutes les tables d'une base de données. Le nom de la base de données sera passé en argument.

**Commande utilisée** : `SHOW TABLES;`

**Exemple d'utilisation** :
```bash
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

---

### 4. First table
**Fichier** : `4-first_table.sql`

Script qui crée une table nommée `first_table` avec deux colonnes :
- `id` : INT
- `name` : VARCHAR(256)

**Commande utilisée** : `CREATE TABLE IF NOT EXISTS`

**Exemple d'utilisation** :
```bash
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 5. Full description
**Fichier** : `5-full_table.sql`

Script qui affiche la description complète de la table `first_table`. N'utilise pas les commandes `DESCRIBE` ou `EXPLAIN`.

**Commande utilisée** : `SHOW CREATE TABLE`

**Exemple d'utilisation** :
```bash
cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 6. List all in table
**Fichier** : `6-list_values.sql`

Script qui liste toutes les lignes de la table `first_table`.

**Commande utilisée** : `SELECT * FROM`

**Exemple d'utilisation** :
```bash
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 7. First add
**Fichier** : `7-insert_value.sql`

Script qui insère une nouvelle ligne dans la table `first_table` avec :
- `id` = 89
- `name` = "Best School"

**Commande utilisée** : `INSERT INTO`

**Exemple d'utilisation** :
```bash
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 8. Count 89
**Fichier** : `8-count_89.sql`

Script qui compte le nombre d'enregistrements avec `id = 89` dans la table `first_table`.

**Commande utilisée** : `SELECT COUNT(*) ... WHERE`

**Exemple d'utilisation** :
```bash
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 9. Full creation
**Fichier** : `9-full_creation.sql`

Script qui crée une table `second_table` avec trois colonnes (`id`, `name`, `score`) et insère quatre enregistrements :
- John (id=1, score=10)
- Alex (id=2, score=3)
- Bob (id=3, score=14)
- George (id=4, score=8)

**Commandes utilisées** : `CREATE TABLE`, `INSERT INTO`

**Exemple d'utilisation** :
```bash
cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 10. List by best
**Fichier** : `10-top_score.sql`

Script qui liste tous les enregistrements de `second_table`, affichant `score` et `name`, triés par score décroissant.

**Commandes utilisées** : `SELECT`, `ORDER BY DESC`

**Exemple d'utilisation** :
```bash
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 11. Select the best
**Fichier** : `11-best_score.sql`

Script qui liste les enregistrements avec un score supérieur ou égal à 10, affichant `score` et `name`, triés par score décroissant.

**Commandes utilisées** : `SELECT`, `WHERE`, `ORDER BY DESC`

**Exemple d'utilisation** :
```bash
cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 12. Cheating is bad
**Fichier** : `12-no_cheating.sql`

Script qui met à jour le score de Bob à 10 dans la table `second_table`. Utilise le champ `name` pour identifier l'enregistrement (pas l'id).

**Commande utilisée** : `UPDATE ... SET ... WHERE`

**Exemple d'utilisation** :
```bash
cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 13. Score too low
**Fichier** : `13-change_class.sql`

Script qui supprime tous les enregistrements avec un score inférieur ou égal à 5 dans la table `second_table`.

**Commande utilisée** : `DELETE FROM ... WHERE`

**Exemple d'utilisation** :
```bash
cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 14. Average
**Fichier** : `14-average.sql`

Script qui calcule la moyenne de tous les scores dans la table `second_table`. Le résultat est affiché dans une colonne nommée `average`.

**Commande utilisée** : `SELECT AVG() AS`

**Exemple d'utilisation** :
```bash
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 15. Number by score
**Fichier** : `15-groups.sql`

Script qui liste le nombre d'enregistrements ayant le même score dans la table `second_table`. Affiche le `score` et le nombre d'occurrences (colonne `number`), triés par nombre décroissant.

**Commandes utilisées** : `SELECT`, `GROUP BY`, `COUNT()`, `ORDER BY DESC`

**Exemple d'utilisation** :
```bash
cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

### 16. Say my name
**Fichier** : `16-no_link.sql`

Script qui liste tous les enregistrements de `second_table` où le champ `name` n'est pas NULL, affichant `score` et `name`, triés par score décroissant.

**Commandes utilisées** : `SELECT`, `WHERE IS NOT NULL`, `ORDER BY DESC`

**Exemple d'utilisation** :
```bash
cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

## Auteur

Projet réalisé dans le cadre de la formation Holberton School.

## Licence

Ce projet est à usage éducatif uniquement.
