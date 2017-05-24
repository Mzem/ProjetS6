Listes des trucs à faire avant de rendre l'appli :
- Ajouter favicon logo DCbrain
- Menu de navigation : traiter les champs "About" et "Contact" + ajouter logo DCbrain tout à gauche

- Améliorer la page d'acceuil : texte d'acceuil + route (index.html en accueil)
- Intégrer le manuel dans l'appli (créer une page "Help") -> lien de dl de notre pdf
- REPARER bouton "go back" : la suppression doit etre faite automatiquement car une fois un mauvais fichier uloadé, on peut quitter l'appli ou aller sur une autre page, pas forcément appuyer sur "go back", et du coup le fichier reste
- graphes (meilleur affichage)
- Fusion About & Contact = About : (lien vers le site de dcbrain)
- Bouton go back role_choix_colonne.html dans resultat_ADD.html (retour à l'étape précédente)
- Histogrammes et secteurs
- .... mettez vos trucs ....

Docstring sphinx:
- Pour mettre à jour la doc, se déplacer dans le repertoire docstring et taper : 
    => make html pour le format html.
    => make latexpdf pour le latex.
- description des modules à compléter
- Ajouter un page installation - build / exécution en local Windows - lubuntu): python 3.x ; flask ; sphinx

Update lien de la documentation : http://deusyss.developpez.com/tutoriels/Python/SphinxDoc/

Refactoring (changements qui ne changeront pas le comportement mais qui rendent l'appli plus propre) :
- gestion flux GET et PUT effectués en même temps (on veut que le PUT)
- js dans dossier js // css dans le dossier css
- gestionFlux, les routes pour l'add (récup json) dans un autre fichier
- code plus propre (indentation html / js ; noms de variable ; commentaires ; espaces, tabulation, sauts de ligne)
- Nettoyer l'appli des docs inutile, arborescence et dossiers
- Deux arborescenses main et tests dans le dossier app
- .... mettez vos trucs ....
