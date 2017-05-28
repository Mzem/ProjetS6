.. Fil Rouge documentation master file, created by Jean-didier Pailleu, Malek Zemni and Sonny Klotz

Documentation du projet Fil Rouge.
***********************************

Description
-----------

Bienvenue sur la documentation technique du projet Fil Rouge.

Dans ce document se trouvent les documentations des éléments de code source de l'application :

* Une API de chargement des données
* Une API d'analyse descriptive des données
* Une interface web exploitant les API

En plus de ce travail, un script ``demoAPI.py`` est mis à disposition.

	Le développement de ce script est motivé par la volonté de donner un exemple d'utilisation des API en passant par l'automatisation de tâches qui seraient lourdes via l'interface web seule.
	
	Mais aussi, il permet de fournir en sortie un compte-rendu statistique réutilisable sur le graphe d'où proviennent les données. 

Ainsi, cette documentation fait également part d'une page de description de ce script, de son utilisation et de ses résultats.

Lancer l'application
--------------------

Avant de commencer
==================

Cette application fonctionne à l'aide d'outils à installer préalablement :

 * `Python 3+ <https://www.python.org/>`_ : langage de programmation principal.
 * `Flask 0.12.x <http://flask.pocoo.org/>`_ : framework d'applciations web en Python.	
 * `Sphinx 1.6.1 <http://www.sphinx-doc.org/en/stable/index.html>`_: génération automatique de documentation.
 * `sphinx_rtd_theme, et guzzle_sphinx_theme` : templates pour sphinx
 
Les cibles makefile peuvent s'exécuter sous linux et windows (fichiers Makefile et make.bat présents)
 
Applet : interface web
=======================

L'instruction qui permet de lancer l'appli est :

.. code-block:: console

	make run
	
.. note::
	
	Veuillez vérifier la version de Python avec l'instruction en ligne de commande. Sous certaines versions linux, il existe deux commandes différentes ``python`` et ``python3`` pour lancer les scripts Python.
	
	Dans le cas où la version n'est pas 3 ou supérieure, veuillez modifier le Makefile manuellement (voir commentaires).

Tests unitaires
===============

Exécuter tous les tests :

.. code-block:: console

	make test

Exécuter les tests du module interface_web :

.. code-block:: console

	make test-interface_web
	
Exécuter les tests du module chargement_des_donnes :

.. code-block:: console

	make test-chargement_des_donnees
	
Exécuter les tests du module add :

.. code-block:: console

	make test-add
	
Génération et lancement de la documentation
===========================================
On rappelle que pour générer la documentation, il faut installer Sphinx et ses modules.

Générer et lancer la documentation au format html :

.. code-block:: console

	make html
	make run-html
	
Générer et lancer la documentation au format pdf :

.. code-block:: console

	make latexpdf
	make run-latexpdf

Documentation
-------------

Interface web
=============

.. toctree::
	:maxdepth: 2
	
	gestionFlux
	choixFichier
	addRoutes

Analyse descriptive de données
==============================
	
.. toctree::
	:maxdepth: 2
	
	addQualitatives
	addQuantitativesContinues
	addQuantitativesDiscretes
	intervalle

Chargement des données
======================
	
.. toctree::
	:maxdepth: 2
	
	verificationFormatFichier
	analyseContenuFichier

Exemples
========

.. toctree::
	:maxdepth: 2
	
	demoAPI
