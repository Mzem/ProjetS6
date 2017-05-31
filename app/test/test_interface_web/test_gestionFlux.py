#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test gestionFlux``
	========================================================


"""
import unittest, sys, os
from shutil import copy

sys.path[:0] = ['../../main']
from interface_web.gestionFlux import app

class test_gestionFlux(unittest.TestCase): 

    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass 

    # initialization logic
    # code exécuté avant chaque test
    def setUp(self):
        pass

    # clean up logic
    # code exécuté après chaque test
    def tearDown(self):
        pass 

    # test fonctions du module gestion des flux 
    
    def test_fenetre_choix_fichier(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200) 

    def test_fenetre_role_choix_colonne(self):
        tester = app.test_client(self)
        response = tester.get('/fenetre_role_choix_colonne/test.csv', content_type='html/text')
        self.assertEqual(response.status_code, 200)  

    def test_fenetre_resultat_ADD(self):
        tester = app.test_client(self)
        response = tester.get('/fenetre_resultat_ADD/test.csv', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_manuel(self):
        tester = app.test_client(self)
        response = tester.get('/manuel/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_remove(self):
        tester = app.test_client(self)
        response = tester.get('/remove/', content_type='html/text')
        self.assertIs(os.path.exists('../../main/interface_web/static/uploads/test.csv'), False)


# runs the unit tests in the module
if __name__ == '__main__':

    os.chdir('../../main')
    unittest.main()
