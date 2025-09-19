from __future__ import annotations


def somme_pairs(nums: list[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs de la liste donnée.
    result = 0
    for number in nums:
        if number % 2 == 0:
            result += number
    return result



def compter_occurrences(items: list[int], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences de `valeur` dans la liste `items`.
    count = 0
    for nb in items:
        if nb == valeur:
            count += 1
    return count



def table_multiplication(n: int) -> list[int]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication de `n` (jusqu'à 10 inclus).
    # 1 - déclarer une variable qui est un tableau vide
    result = []
    # 2 - Boucle pour remplir le tableau
        # Faire une boucle pour laquelle i va de 1 à 10
        # Ajoute n * i à result
    i = 1
    while i < 11:
        result.append(i * n)
        i += 1
        
    # 3 - retourner le tableau
    return result


def trouver_maximum(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur maximale dans la liste.
    result = None
    for value in nums:
        if result is None:
            result = value
        elif value > result:
            result = value
    return result


def calculer_moyenne(nums: list[int]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des valeurs dans la liste.
    if len(nums) == 0:
        return 0
    value = sum(nums) / len(nums)
    return value


def compter_negatifs(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre d'entiers négatifs dans la liste.
    result = 0
    for value in nums:
        if value < 0:
            result += 1
    return result


def compter_mots(phrase: str) -> int:
    # TODO: Implémentez une fonction pour compter le nombre de mots dans une chaîne de caractères donnée.
    if phrase == "":
        return 0
    number = phrase.split(" ")
    word_nb = len(number)
    return word_nb


def trouver_plus_long(items: list[str]) -> str:
    # TODO: Implémentez une fonction pour trouver et retourner le mot le plus long dans une liste de chaînes de caractères.
    
    if len(items) == 0: 
        return ""

    longest_word = items[0]

    for word in items:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def convertir_majuscule(items: list[str]) -> list[str]:
    # TODO: Implémentez une fonction pour convertir toutes les chaînes de la liste en majuscules.
    if len(items) == 0: 
        return ""

    maj_word = []

    for words in items:     
        words = items.upper()
        maj_word = words

    return maj_word


def compter_mots_commencant_par(items: str, lettre: str) -> int:
    # TODO: Implémentez une fonction pour compter les mots commençant par une lettre donnée.

# Si le mot commence par une lettre donnée alors :
    # Ajoute +1 au décompte
# Si non n'ajoute rien au décompte
    # Attention à la casse
    items = items.split()
    
    if len(items) == 0:
        return 0

    result = 0

    for word in items:
        if word.lower().startswith(lettre.lower()):
            result += 1

    return result


def trouver_mot_finissant_par(items: str, suffixe: str) -> list[str]:
    # TODO: Implémentez une fonction pour trouver tous les mots qui se terminent par un suffixe donné dans la liste.
    items = items.split(" ")
    
    if len(items) == 0:
        return 0
    result = []
    
    for word in items:
        if word.lower().endswith(suffixe.lower()):
            result.append(word)
    return result


def compter_caracteres(s: str, c: str) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre total de caractères dans la chaîne.
    # Créer une variable pour stocker le résultat intialisée à 0
    # Parcourir tous les caractères
        # Si le caractères est trouvé, on ajoute 1
        # Si non, on n'ajoute rien
    # Retourner le résultat

    result = 0

    for lettre in s:
        if lettre == c:
            result += 1

    return result


def inverser_chaine(s: str) -> str:
    # TODO: Implémentez une fonction pour inverser et retourner la chaîne de caractères donnée.
    # Prendre en compte si la chaine de caractère est vide
    # Créer une variable pour stocker le résultat
    # Inverser la chaine de caractères
    # Retourner la chaine de caractères inversée

    if s == "":
        return ""

    result = s[::-1]

    return result

def trouver_occurrences_chaine(s: str, c: str) -> int:
    # TODO: Implémentez une fonction pour compter les occurrences d'un caractère donné dans une chaîne.
    # Créer une variable pour stocker le résultat
    # Parcourir tous les caractères
        # Comparer au caractère donné
        # Stocker la réponse dans la variable préalablement crée
    # Retourner le résultat
    
    result = s.count(c)

    return result

# tuples
def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un tuple donné.
    # Pour savoir si un nb est pair : modulo
    # Parcourir les valeurs du tuple
        # Reconnaitre les nombres pairs
        # Les extraires ?
        # Additionner les nombres pairs
    # retourner le résultat

    result = 0

    for number in nums:
        if number % 2 == 0:
            result = number + result
    
    return result


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences d'une valeur dans un tuple donné.
    count = 0
    for nb in items:
        if nb == valeur:
            count += 1
    return count


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de tuple.
    result = ()
    y = 0

    i = 1
    while i < 11:
        y = (i * n,)
        result += y
        i +=1
    return result


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un tuple.
    result = ()

    return max(nums)


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des nombres dans un tuple.
    if len(nums) == 0:
        return 0
    value = sum(nums) / len(nums)
    return value

# sets

def somme_pairs_sets(nums: set[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un set donné.
    result = 0
    for number in nums:
        if number % 2 == 0:
            result += number
    return result

def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    # TODO: Cette fonction vérifiera simplement si `valeur` existe puisque les sets ne permettent pas les doublons.
    count = 0
    for nb in items:
        if nb == valeur:
            count += 1
    return count


def table_multiplication_sets(n: int) -> set[int]:
    # TODO: Implémentez une fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de set.
    result = []
    i = 1
    while i < 11:
        result.append(i * n)
        i += 1

    return set(result)

def trouver_maximum_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un set.
    raise NotImplementedError


def compter_negatifs_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre de nombres négatifs dans un set.
    raise NotImplementedError

# dictionnaires

def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    # TODO: Implémentez une fonction pour ajouter une clé et sa valeur dans un dictionnaire.
    raise NotImplementedError


def supprimer_element(d: dict, cle: str) -> dict:
    # TODO: Implémentez une fonction pour supprimer une clé et sa valeur d'un dictionnaire.
    raise NotImplementedError


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    # TODO: Implémentez une fonction qui fusionne deux dictionnaires et renvoie le résultat.
    # Les valeurs de `d2` remplaceront celles de `d1` en cas de doublons.
    raise NotImplementedError


def inverser_dictionnaire(d: dict) -> dict:
    # TODO: Implémentez une fonction pour inverser un dictionnaire, échangeant les clés et les valeurs.
    # Note: Si des valeurs duplicatées existent, une erreur ou un comportement spécifique doit être défini.
    raise NotImplementedError


def compter_valeurs(d: dict) -> int:
    # TODO: Implémentez une fonction pour compter combien de paires clé-valeur sont dans le dictionnaire.
    raise NotImplementedError


def trouver_valeur_maximale(d: dict) -> any:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur la plus grande dans un dictionnaire.
    raise NotImplementedError


def trouver_cle_par_valeur(d: dict, valeur: any) -> list[str]:
    # TODO: Implémentez une fonction pour retourner une liste de toutes les clés correspondant à une valeur donnée.
    raise NotImplementedError


def verifier_cle_existe(d: dict, cle: str) -> bool:
    # TODO: Implémentez une fonction qui vérifie si une clé existe dans le dictionnaire.
    raise NotImplementedError


def valeurs_uniques(d: dict) -> set:
    # TODO: Implémentez une fonction qui retourne toutes les valeurs uniques dans un dictionnaire sous forme de set.
    raise NotImplementedError


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    # TODO: Implémentez une fonction pour mettre à jour une valeur associée à une clé existante ou en ajouter une nouvelle.
    raise NotImplementedError
