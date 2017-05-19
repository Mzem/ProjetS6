#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test gestionFlux``
	========================================================


"""
import unittest 
from flask_testing import TestCase, LiveServerTestCase
from flask_testing.utils import ContextVariableDoesNotExist
import sys
sys.path[:0] = ['../']
from interface_web.gestionFlux import *

class gestionFluxTest(unittest.TestCase): 

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
    def test_index(self):
        self.assert200(self.client.get("/"))
    
    def test_FileWithDragDrop(self):
        return True
        

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
