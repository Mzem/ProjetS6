Plan démo (15:00) :
- Présentation de l'appli, annonce du plan : démo de l'appli, de la doc et des tests (00:30) JD
(JD passe sur l'ordi)
- Démo, montrer les qualités de l'appli :
	
	- Manuel et about
	- Un cas idéal : drag drop (2:00) MALEK
	
	
	Mainenant je vais expliquer plus en détails ma fenetre
	- Différents types de fichiers CSV (1:00) MALEK
	- Parler des filtres : charger le fichierDemo MALEK (3:00)




















Lancer l'application
--------------------

Avant de commencer
==================

Cette application fonctionne à l'aide d'outils à installer préalablement :

 * `Python 3+ <https://www.python.org/>`_ : langage de programmation principal.
 * `Flask 0.12.x <http://flask.pocoo.org/>`_ : framework d'applciations web en Python.	
 * `Sphinx 1.6.1 <http://www.sphinx-doc.org/en/stable/index.html>`_: génération automatique de documentation.
 * `sphinx_rtd_theme, et guzzle_sphinx_theme` : templates pour sphinx
 
Les cibles makefile peuvent s'exécuter sous linux et windows dans le dossier 'app/'(fichiers Makefile et make.bat présents)
 
Applet : interface web
=======================

L'instruction qui permet de lancer l'appli est :
-	make run

Veuillez vérifier la version de Python avec l'instruction en ligne de commande. Sous certaines versions linux, il existe deux commandes 
différentes ``python`` et ``python3`` pour lancer les scripts Python.
Dans le cas où la version n'est pas 3 ou supérieure, veuillez modifier le Makefile manuellement (voir commentaires).

Tests unitaires
===============

Exécuter tous les tests :
-	make test

Exécuter les tests du module interface_web :
-	make test-interface_web
	
Exécuter les tests du module chargement_des_donnes :
-	make test-chargement_des_donnees
	
Exécuter les tests du module add :
-	make test-add
	
Génération et lancement de la documentation
===========================================
On rappelle que pour générer la documentation, il faut installer Sphinx et ses modules.

Générer et lancer la documentation au format html :
-	make html
-	make run-html (Sur windows lance par défaut sur google chrome, si vous utilisez un autre navigateur veuillez le changer dans make.bat)
	
Générer et lancer la documentation au format pdf :
-	make latexpdf
-	make run-latexpdf
