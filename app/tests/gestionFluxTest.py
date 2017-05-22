#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test gestionFlux``
	========================================================


"""
import unittest, sys, os
from flask_testing import TestCase, LiveServerTestCase
from shutil import copy2

sys.path[:0] = ['../']
from interface_web.gestionFlux import app

class gestionFluxTest(unittest.TestCase): 

    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        copy2('./static/test.csv', '../interface_web/static/uploads/') 

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

    # test fonctions du module Add_qualitatives 
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_fenetre_choix_fichier(self):
        tester = app.test_client(self)
        response = tester.get('/fenetre_choix_fichier/test.csv', content_type='html/text')
        self.assertEqual(response.status_code, 200)         

    def test_fenetre_role_choix_colonne(self):
        tester = app.test_client(self)
        response = tester.get('/fenetre_role_choix_colonne/', content_type='html/text')
        self.assertEqual(response.status_code, 200)  

    def test_fenetre_resultat_ADD(self):
        tester = app.test_client(self)
        response = tester.get('/fenetre_resultat_ADD/', content_type='html/text')
        self.assertEqual(response.status_code, 200)         
    
    def test_remove(self):
        tester = app.test_client(self)
        os.chdir('../')
        response = tester.get('/remove/test.csv', content_type='html/text')
        self.assertIs(os.path.exists('interface_web/static/uploads/test.csv'), False)

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
