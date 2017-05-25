Listes des trucs à faire avant de rendre l'appli :
- CENTRER MENUS NAV
- Envoi echantillon à ADD ajax
- graphes (meilleur affichage) - Sonny
- Histogrammes et secteurs - Sonny
- script pour que tous les tests se lancent en une ligne de commande (et ajouter dans la doc voir plus bas)
- Times Series et Boxplot graphes
- .... mettez vos trucs ....

Docstring sphinx:
- Pour mettre à jour la doc, se déplacer dans le repertoire docstring et taper : 
    => make html pour le format html.
    => make latexpdf pour le latex.
- description des modules à compléter
- Ajouter une partie installation - build en local Windows - lubuntu): python 3.x ; flask ; sphinx
- Ajouter une partie exécution : lignes de commandes pour l'appli, pour la demo, pour les tests

Update lien de la documentation : http://deusyss.developpez.com/tutoriels/Python/SphinxDoc/

Refactoring (changements qui ne changeront pas le comportement mais qui rendent l'appli plus propre) :
- gestion flux GET et PUT effectués en même temps (on veut que le PUT)
- js dans dossier js // css dans le dossier css
- code plus propre (indentation html / js ; noms de variable ; commentaires ; espaces, tabulation, sauts de ligne)
- Nettoyer l'appli des docs inutile, arborescence et dossiers
- Deux arborescenses main et tests dans le dossier app (A ne pas faire sinon je dois changer tout mes tests)
- .... mettez vos trucs ....
