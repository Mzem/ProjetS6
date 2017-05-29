Plan d�mo (15:00) :
- Pr�sentation de l'appli, annonce du plan : d�mo de l'appli, de la doc et des tests (00:30) JD
(JD passe sur l'ordi)
- D�mo, montrer les qualit�s de l'appli :
	
	- Manuel et about
	- Un cas id�al : drag drop (2:00) MALEK
	
	
	Mainenant je vais expliquer plus en d�tails ma fenetre
	- Diff�rents types de fichiers CSV (1:00) MALEK
	- Parler des filtres : charger le fichierDemo MALEK (3:00)
	
	- Decrire ta fenetre, � partir des filtres (03:00)
	- Export et pr�sentation du script (01:00)
	
- Documentation (02:00)
- Tests (02:00)

- Conclusion (00:30)




















Lancer l'application
--------------------

Avant de commencer
==================

Cette application fonctionne � l'aide d'outils � installer pr�alablement :

 * `Python 3+ <https://www.python.org/>`_ : langage de programmation principal.
 * `Flask 0.12.x <http://flask.pocoo.org/>`_ : framework d'applciations web en Python.	
 * `Sphinx 1.6.1 <http://www.sphinx-doc.org/en/stable/index.html>`_: g�n�ration automatique de documentation.
 * `sphinx_rtd_theme, et guzzle_sphinx_theme` : templates pour sphinx
 
Les cibles makefile peuvent s'ex�cuter sous linux et windows dans le dossier 'app/'(fichiers Makefile et make.bat pr�sents)
 
Applet : interface web
=======================

L'instruction qui permet de lancer l'appli est :
-	make run

Veuillez v�rifier la version de Python avec l'instruction en ligne de commande. Sous certaines versions linux, il existe deux commandes 
diff�rentes ``python`` et ``python3`` pour lancer les scripts Python.
Dans le cas o� la version n'est pas 3 ou sup�rieure, veuillez modifier le Makefile manuellement (voir commentaires).

Tests unitaires
===============

Ex�cuter tous les tests :
-	make test

Ex�cuter les tests du module interface_web :
-	make test-interface_web
	
Ex�cuter les tests du module chargement_des_donnes :
-	make test-chargement_des_donnees
	
Ex�cuter les tests du module add :
-	make test-add
	
G�n�ration et lancement de la documentation
===========================================
On rappelle que pour g�n�rer la documentation, il faut installer Sphinx et ses modules.

G�n�rer et lancer la documentation au format html :
-	make html
-	make run-html (Sur windows lance par d�faut sur google chrome, si vous utilisez un autre navigateur veuillez le changer dans make.bat)
	
G�n�rer et lancer la documentation au format pdf :
-	make latexpdf
-	make run-latexpdf