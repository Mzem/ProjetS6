import unittest 

class addQualitativesTest(unittest.TestCase): 

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
    # code that is executed before each test
    def setUp(self):
        pass 

    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        pass 

    # test fonction du module Add_qualitatives        
    def test_calculEffectifs(self):
        return True 
        
    def test_calculEffectifsCumules(self):
        return True 
        
    def test_calculFrequences(self):
        return True 
        
    def calculFrequencesCumules(self):
        return True 

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
