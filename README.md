Listes des trucs à faire avant de rendre l'appli :
- Ajouter favicon logo DCbrain
- Menu de navigation : traiter les champs "About" et "Contact" + ajouter logo DCbrain tout à gauche
- Améliorer la page d'acceuil : texte d'acceuil + route (je pense que index.html directement (sans route) c'est mieux que /fenetre_choix_fichier, on essaye de faire un truc propre meme si c'est pas ça dans les specs)
- Intégrer le manuel dans l'appli (dans la page "About" ou lui créer une page "Help")
- REPARER bouton "go back" : la suppression doit etre faite automatiquement car une fois un mauvais fichier uloadé, on peut quitter l'appli ou aller sur une autre page, pas forcément appuyer sur "go back", et du coup le fichier reste
- .... mettez vos trucs ....



Update lien de la documentation : http://deusyss.developpez.com/tutoriels/Python/SphinxDoc/

J'avais un problème que je voulais poster dans issue mais je l'ai corrigé, pas besoin de check les issues comme je le dis dans mon commit

- Mon fichier miniatures.js n'etait pas chargé par la page

- J'ai corrigé l'url, mais mes graphes avec fichiers json ne marchaient pas

- J'ai changé le js pour ne pas utiliser les fichiers json et tester avec les données directes dans le script

- Ca marchait toujours pas et il me cherchait encore les fichiers json et le script ne se chargeait toujours pas

- J'ai vidé le cache du navigateur et relancer et la tout fonctionne

:warning: Les scripts JavaScript se sauvegardent dans le cache pour gagner en rapidité,  si vous voulez tester des modifs, supprimez d'abord le cache et check les outils de dev du navigateur c'est archi utile
