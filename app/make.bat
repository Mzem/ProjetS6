
@echo off

REM Règle pour le lancement de l'application
:run
cd main\
start python runserver.py
goto end

REM Règle pour supprimer les .pyc et lancer les tests
:all
test
goto end

REM Règles pour le lancement des tests
:test-interface_web
cd test\test_interface_web
start python -m unittest discover
goto end

:test-add
cd test\test_add
start python -m unittest discover
goto end

:test-chargement_des_donnees
cd test\test_chargement_des_donnees
start python -m unittest discover
goto end

:test
cd test\test_interface_web
start python -m unittest discover
cd ..\test_add
start python -m unittest discover
cd..\test_chargement_des_donnees
start python -m unittest discover
cd ..
goto end

REM Règle pour générer et afficher la documentation au format html
:doc-html
cd doc/
start make html
google-chrome doc/build/html/index.html
goto end

REM Règle pour générer la documentation au format latex
:doc-latexpdf
cd doc/
start make latexpdf
xdg-open doc/build/latex/FilRouge.pdf &
goto end

:end
cd ..
popd
