#TODO : faire un programme qui permet à un enseingant
#TODO : d'entrer des noms d'élèves, des matière et des notes
#TODO : et enregister les bulletins dans un ou des fichiers
#TODO : on doit avoir plusieurs notes par étudiant par matière
"""
bulletins = {
    "Jo": {
        "Math": [12, 14, 18],
        "Français": [15, 11, 16],
        "Histoire": [17, 10, 19]
    }
    "Aline": {
        ...
    }
}
"""
# bulletin = {}
# while true
    # demander prenom
    # bulletin[prenom] = {}
    # while true
        # demander matière
        # bulletin[prenom][matière] = []
        #while true
            #demander note
            #bulletin[prenom][matière].append(note)

            # TODO : breaks
# sauvegarder bulletin dans un fichier
import json
bulletin = {}
while True:
    prenom = input("Prenom: ")
    if prenom == "":
        break
    bulletin[prenom] = {}
    while True:
        matiere = input("Matière: ")
        if matiere == "":
            break
        bulletin[prenom][matiere] = []
        while True:
            note = int(input("Note: ")) # TODO : ajouter la gestion d'erreur
            if note == -1:
                break
            bulletin[prenom][matiere].append(note)
with open("ecole/ecole.json", "w", encoding="utf-8") as fichier:
    fichier.write(json.dumps(bulletin, ensure_ascii=False, indent=4))
