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
 
Applet sur serveur local
========================

Commande + description

L'instruction qui lance l'appli (à modifier avec les bons chemins)
D'ailleurs est-ce que runserver c'est du local, je comprends pas trop tout ça

.. code-block:: console
	
	python runserver.py
	
Applet sur serveur distant
==========================

connexion ssh sur une machine à distance, est-ce qu'on le met?

Tests unitaires
===============

Commande


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
