#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module choixFichier``
	========================================================


"""
import unittest, io, sys, os
from io import BytesIO

sys.path.append('../../main')
from interface_web.choixFichier import *
from interface_web.gestionFlux import app

class test_choixFichier(unittest.TestCase): 

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

    # test fonctions du module Add_qualitatives 
    def test_FileWithSGF(self):
        tester = app.test_client(self)
        os.chdir('../')
        data = {'file': (BytesIO(b'my file contents'), 'test.csv')}
        response = tester.post('/FileWithSGF', buffered=True,
                         content_type='multipart/form-data',
                             data=data)
        self.assertEqual(response.status_code, 301)  # On vérifie qu'il y a bien redirection
      
    
    def test_FileWithDragDrop(self):
        tester = app.test_client(self)
        os.chdir('../')
        data = {'file': (BytesIO(b'my file contents'), 'test.csv')}
        response = tester.post('/FileWithDragDrop', buffered=True,
                    content_type='multipart/form-data',
                         data=data)
        self.assertEqual(response.status_code, 301) # On vérifie qu'il y a bien redirection
               
        

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
