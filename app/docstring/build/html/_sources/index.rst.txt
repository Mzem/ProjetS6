.. File Rouge documentation master file, created by

Bienvenue sur la documentation du projet Fil Rouge!
====================================================

Installation
------------

La constrcution de l'application et de sa documentation se repose sur trois outils :
 * `Python <https://www.python.org/>`_ à installer python sous une version 3 ou ultérieure.
 * `Flask <http://flask.pocoo.org/>`_ sous sa dernière version stable, 0.12.x .
 * `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ sous sa dernère version stable, 1.6.1 .

Exécution
----------

Applet:
Je sais pas ce que notre commande fait : exécution sur serveur local?

.. code-block:: console
	
	python runserver.py

exécution à distance? si on le fait ??

Tests unitaires:

.. code-block:: console
	
	python -m unittest

Modules
-------
.. toctree::
	:maxdepth: 2

	gestionFlux
	choixFichier
	addRoutes
	addQualitatives
	addQuantitativesContinues
	addQuantitativesDiscretes
	intervalle
	verificationFormatFichier
	analyseContenuFichier
