.PHONY: clean-pyc test 

# Règle pour le lancement des tests et du nettoyage
all: clean-pyc test

# Règles pour le lancement des tests
test-interface_web:
	cd test/test_interface_web; python -m unittest discover

test-add:
	cd test/test_add; python -m unittest discover

test-chargement_des_donnees:
	cd test/test_chargement_des_donnees; python3 -m unittest discover

test: test-add test-chargement_des_donnees test-interface_web 

# Règle pour le lancement de l'application
run:
	cd main/; python runserver.py

#Règle pour générer la documentation au format html
doc-html:
	cd doc/; make html

#Règle pour générer la documentation au format latex
doc-latexpdf:
	cd doc/; make latexpdf

#Règle pour néttoyer des fichiers de compilation
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
