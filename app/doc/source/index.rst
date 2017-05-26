.. Fil Rouge documentation master file, created by Jean-didier Pailleu, Malek Zemni and Sonny Klotz

Documentation du projet Fil Rouge.
***********************************

Lancer l'application
--------------------

Avant de commencer
==================

Cette application fonctionne à l'aide d'outils à installer préalablement :

 * `Python 3+ <https://www.python.org/>`_ : langage de programmation principal.
 * `Flask 0.12.x <http://flask.pocoo.org/>`_ : framework d'applciations web en Python.	
 * `Sphinx 1.6.1 <http://www.sphinx-doc.org/en/stable/index.html>`_: génération automatique de documentation.
 
Exécution sur serveur local
===========================

L'instruction qui lance l'appli (à modifier avec les bons chemins)
D'ailleurs est-ce que runserver c'est du local, je comprends pas trop tout ça

.. code-block:: console
	
	python runserver.py
	
Exécution sur serveur distant
=============================

connexion ssh sur une machine à distance, est-ce qu'on le met?

Tests unitaires
===============

L'instruction qui lance les tests (à modifier avec les bons chemins)

.. code-block:: console
	
	python -m unittest


Modules
-------

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
