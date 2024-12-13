import unittest
# import tests_12_1
import tests_12_3


calcST = unittest.TestSuite()
# calcST.addTest(unittest.makeSuite(test_12_1.TestRunner))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
