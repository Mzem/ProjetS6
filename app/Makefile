.PHONY: clean-pyc test 

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

#Règle pour générer et afficher la documentation au format html
html:
	cd doc/; make html
	
run-html:
	google-chrome doc/build/html/index.html

#Règle pour générer la documentation au format latex
latexpdf:
	cd doc/; make latexpdf

run-latexpdf:
	xdg-open doc/build/latex/FilRouge.pdf &

#Règle pour néttoyer des fichiers de compilation
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
