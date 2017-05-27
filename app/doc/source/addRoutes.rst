************************
addRoutes.py
************************

Description
===========

Les fonctions de ce fichiers servent à répondre aux requêtes client pour récupérer des fichiers sur le serveur selon le modèle ``ajax``.

En effet, après la requête, le serveur n'envoie pas toute une page web, mais seulement les données qui intéressent le navigateur.

Cette technique permet de communiquer plus efficacement les données entre le client et le serveur.

De plus, le format de fichier ``json`` est un format léger, et est donc très adapté pour ce cas de figure.

Les fonctions
=============

.. automodule:: interface_web.addRoutes

.. autofunction:: iStats

.. autofunction:: timeSeries

.. autofunction:: distribution

.. autofunction:: distributionCumulative

.. autofunction:: boxplot
