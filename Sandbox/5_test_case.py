import unittest

# Mention custom decorators

#@f1(arg)
#def func(): pass
# ->
#def func(): pass
#func = f1(arg)(func)

#@f2
#def func(): pass
# ->
#def func(): pass
#func = f2(func)

#Mention custom decorators
def customSkip(skip):
    if skip == True:
        return lambda func: func
    else:
        return unittest.skip("skip enabled")

# class to test
class Add():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

class Multiply(unittest.TestCase):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mul(self):
        return self.a*self.b

#@unittest.skip("skipping class")
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.a = Add(5, 10)

    def tearDown(self):
        pass

    def runTest(self):
        self.assertEqual(self.a.add(), 15)

class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.m = Multiply(5, 10)

    def tearDown(self):
        pass

    def test_equal(self):
        self.assertEqual(self.m.mul(), 50)

    def test_greaterThan(self):
       self.assertTrue(self.m.mul() > 40)

    #@customSkip(False)
    def test_lessThan(self):
       self.assertFalse(self.m.mul() < 40)

    #@unittest.skip("skipping function")
    def test_divByZero(self):
       with self.assertRaises(ZeroDivisionError):
           self.m.mul()/0

    @unittest.expectedFailure
    def test_fail(self) :
        self.assertTrue(False);

#Creating a custom test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMultiply('test_equal'))
    suite.addTest(TestMultiply('test_greaterThan'))
    suite.addTest(TestAdd('runTest'))
    return suite

# run test
if __name__ == '__main__':
    #unittest.main()

    # 1st try - loading a suite from test cases
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiply)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    # Create a test suite
    #suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMultiply)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    #alltests = unittest.TestSuite([suite1, suite2])
    #unittest.TextTestRunner(verbosity=2).run(alltests)

    # Creating a custom test suite
    unittest.TextTestRunner(verbosity=2).run(suite())


