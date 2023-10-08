#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = input("Entrez 10 valeurs: ")
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = input("Entrez les mots: ")
    return sorted(list(words[0])) == sorted(list(words[1])) # sorted(list) sort la liste et renvoie le résultat
                                                            #liste.sort() sort la liste mais ne renvoie aucun résultat

def contains_doubles(items: list) -> bool:
    ensemble = set(items)
    return len(items) != len(ensemble)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    grades = dict()
    for key, values in student_grades.items():
        moyenne_values = int(sum(values) / len(values))
        grades[key] = moyenne_values

    for key, value in grades.items():
        if value == max(list(grades.values())):
            best_student = {key : value}
    
    return best_student
    
    

         
    


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    used_char = dict()
    for c in sentence:
        used_char[c] = sentence.count(c) # la clé a une valeur unique dans un dictionnaire

    counting = []
    for key, value in used_char.items():
        if value > 5:
            counting.append(key)
    
    counting.sort(reverse=True)
    return counting


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = input("Veuillez entrer le nom de votre recette: ")
    ingredients = input("Veuillez entrer les ingrédients: ")
    return {nom : ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    if ingredients in recette.values():
        print(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    print(frequence("J'adore mon baccalaureat en genie informatique/logiciel"))