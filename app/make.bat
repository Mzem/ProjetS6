
@echo off

if "%1" == "run" goto :run
if "%1" == "test-interface_web" goto :test-interface_web
if "%1" == "test-add" goto :test-add
if "%1" == "test-chargement_des_donnees" goto :test-chargement_des_donnees
if "%1" == "test" goto :test
if "%1" == "html" goto :html
if "%1" == "latexpdf" goto :latexpdf
if "%1" == "run-html" goto :run-html
if "%1" == "run-latexpdf" goto :run-latexpdf
if "%1" == "clean-pyc" goto :clean-pyc

REM Commande non reconnue!
goto :end

REM Règle pour le lancement de l'application
:run
cd main\
python runserver.py & cd ..
goto :end

REM Règles pour le lancement des tests
:test-interface_web
cd test\test_interface_web
python test_gestionFlux.py
python test_choixFichier.py
cd ..\..
goto :end

:test-add
cd test\test_add
python -m unittest discover
cd ..\..
goto :end

:test-chargement_des_donnees
cd test\test_chargement_des_donnees
python -m unittest discover
cd ..\..
goto :end

:test
cd test\test_interface_web
python test_gestionFlux.py
python test_choixFichier.py
cd ..\test_add
python -m unittest discover
cd..\test_chargement_des_donnees
python -m unittest discover
cd ..\..
goto :end

REM Règle pour générer et afficher la documentation au format html
:html
cd doc\
make html & cd ..
goto :end

:run-html
cd doc\build\html\
start chrome.exe index.html & cd ..\..\..\
goto :end

:run-latexpdf
cd doc\build\latex\
FilRouge.pdf & cd ..\..\..\
goto :end

REM Règle pour générer la documentation au format latex
:latexpdf
cd doc\
make latexpdf & cd ..
goto :end

:clean-pyc
del /s *.pyc
del /s *.pyo
del /s *~
:end
