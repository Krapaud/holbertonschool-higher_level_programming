#!/usr/bin/python3
"""
Script de test pour vérifier tes réponses.
Ce script te permet de tester chaque question avant de soumettre tes réponses.
"""

def test_question(question_num, description, code_to_test, expected_hint=None):
    """Affiche une question et permet de la tester"""
    print(f"\n{'='*60}")
    print(f"Question {question_num}: {description}")
    print(f"{'='*60}")
    print("\nCode à tester:")
    print(code_to_test)
    print("\nRésultat:")
    exec(code_to_test)
    if expected_hint:
        print(f"\nIndice: {expected_hint}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    print("Script de test pour python-everything_is_object")
    print("=" * 60)
    print("Utilise ce script pour tester chaque question avant de répondre!")
    print("=" * 60)
    
    # Question 0
    print("\n0. Quelle fonction affiche le type d'un objet ?")
    print("Test:")
    test_question(0, "Afficher le type d'un objet",
                  """a = 42
print(type(a))
b = "Hello"
print(type(b))""",
                  "Regarde le nom de la fonction utilisée (sans les parenthèses)")
    
    # Question 1
    print("\n1. Quelle fonction retourne l'identifiant (adresse mémoire) d'un objet ?")
    test_question(1, "Obtenir l'identifiant d'un objet",
                  """a = 42
print(id(a))
b = 42
print(id(b))""",
                  "Regarde le nom de la fonction qui donne l'identifiant unique")
    
    # Questions 2-5 : Comparaison d'entiers
    print("\n2-5. Comprendre quand deux variables pointent vers le même objet")
    test_question(2, "a = 89; b = 100",
                  """a = 89
b = 100
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "Sont-ils le même objet ?")
    
    test_question(3, "a = 89; b = 89",
                  """a = 89
b = 89
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "Python optimise les petits entiers!")
    
    test_question(4, "a = 89; b = a",
                  """a = 89
b = a
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "Assignation directe: b pointe vers le même objet que a")
    
    test_question(5, "a = 89; b = a + 1",
                  """a = 89
b = a + 1
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "a + 1 crée un nouvel objet")
    
    # Questions 6-9 : Chaînes de caractères
    print("\n6-9. Comparaison de chaînes (== vs is)")
    test_question(6, 's1 = "Best School"; s2 = s1; print(s1 == s2)',
                  """s1 = "Best School"
s2 = s1
print(s1 == s2)""",
                  "== compare les valeurs")
    
    test_question(7, 's1 = "Best"; s2 = s1; print(s1 is s2)',
                  """s1 = "Best"
s2 = s1
print(s1 is s2)""",
                  "Assignation directe")
    
    test_question(8, 's1 = "Best School"; s2 = "Best School"; print(s1 == s2)',
                  """s1 = "Best School"
s2 = "Best School"
print(s1 == s2)""",
                  "Les valeurs sont-elles égales ?")
    
    test_question(9, 's1 = "Best School"; s2 = "Best School"; print(s1 is s2)',
                  """s1 = "Best School"
s2 = "Best School"
print(s1 is s2)""",
                  "Python optimise les chaînes identiques (interning)")
    
    # Questions 10-13 : Listes
    print("\n10-13. Listes : mutable objects")
    test_question(10, 'l1 = [1, 2, 3]; l2 = [1, 2, 3]; print(l1 == l2)',
                  """l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)""",
                  "Les valeurs sont-elles égales ?")
    
    test_question(11, 'l1 = [1, 2, 3]; l2 = [1, 2, 3]; print(l1 is l2)',
                  """l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)""",
                  "Deux listes créées séparément = objets différents")
    
    test_question(12, 'l1 = [1, 2, 3]; l2 = l1; print(l1 == l2)',
                  """l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)""",
                  "l2 pointe vers la même liste que l1")
    
    test_question(13, 'l1 = [1, 2, 3]; l2 = l1; print(l1 is l2)',
                  """l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)""",
                  "Même référence")
    
    # Questions 14-15 : Modification de listes
    print("\n14-15. Modification de listes")
    test_question(14, 'l1.append(4) - modification in-place',
                  """l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)""",
                  "append modifie la liste existante")
    
    test_question(15, 'l1 = l1 + [4] - crée une nouvelle liste',
                  """l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)""",
                  "l1 + [4] crée une nouvelle liste et réassigne l1")
    
    # Questions 16-18 : Fonctions et mutabilité
    print("\n16-18. Passage d'arguments aux fonctions")
    test_question(16, 'Incrémentation d\'un entier (immutable)',
                  """def increment(n):
    n += 1

a = 1
increment(a)
print(a)""",
                  "Les entiers sont immutables")
    
    test_question(17, 'Ajout à une liste (mutable)',
                  """def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)""",
                  "Les listes sont mutables")
    
    test_question(18, 'Réassignation dans une fonction',
                  """def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)""",
                  "La réassignation locale ne change pas l'objet original")
    
    # Questions 20-23 : Tuples
    print("\n20-23. Qu'est-ce qu'un tuple ?")
    test_question(20, 'a = ()',
                  """a = ()
print(type(a))
print(isinstance(a, tuple))""",
                  "Parenthèses vides = tuple vide")
    
    test_question(21, 'a = (1, 2)',
                  """a = (1, 2)
print(type(a))
print(isinstance(a, tuple))""",
                  "Parenthèses + virgule = tuple")
    
    test_question(22, 'a = (1)',
                  """a = (1)
print(type(a))
print(isinstance(a, tuple))""",
                  "Parenthèses seules ne suffisent pas!")
    
    test_question(23, 'a = (1,)',
                  """a = (1,)
print(type(a))
print(isinstance(a, tuple))""",
                  "La virgule finale fait le tuple")
    
    # Questions 24-26 : Optimisation des tuples
    print("\n24-26. Optimisation des tuples")
    test_question(24, 'a = (1); b = (1); a is b',
                  """a = (1)
b = (1)
print(f"a is b: {a is b}")
print(f"type(a): {type(a)}, type(b): {type(b)}")""",
                  "Attention: (1) n'est PAS un tuple!")
    
    test_question(25, 'a = (1, 2); b = (1, 2); a is b',
                  """a = (1, 2)
b = (1, 2)
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "Tuples créés séparément")
    
    test_question(26, 'a = (); b = (); a is b',
                  """a = ()
b = ()
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")""",
                  "Python optimise les tuples vides")
    
    # Questions 27-28 : ID des listes
    print("\n27-28. Modification de listes et ID")
    test_question(27, 'a = a + [5] - nouvelle liste',
                  """a = [1, 2, 3, 4]
print(f"id(a) avant: {id(a)}")
a = a + [5]
print(f"id(a) après: {id(a)}")
print(f"L'ID a changé: {True}")""",
                  "a + [5] crée une nouvelle liste")
    
    test_question(28, 'a += [4] - modification in-place',
                  """a = [1, 2, 3]
print(f"id(a) avant: {id(a)}")
a += [4]
print(f"id(a) après: {id(a)}")
print(f"L'ID est le même: {True}")""",
                  "+= modifie la liste existante (pour les mutables)")
    
    print("\n" + "="*60)
    print("Maintenant, essaie de remplir tes fichiers de réponses!")
    print("Utilise Python pour expérimenter avant de répondre.")
    print("="*60)
