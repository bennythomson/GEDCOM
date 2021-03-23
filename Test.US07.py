import unittest
import sys
sys.path.append('../')
from datetime import date
import working_mc

class TestUS07(unittest.TestCase):
    def testIs4(self):
        # this will test if

        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Indiv('I12', 'Buck /Simpson/', 'M', '1866-07-02', 'T', 'None', 'None', 'F5')

        # test to see if correct case runs from user story
        self.assertEqual(working_mc.less_than_150(individual), 'I12')

if __name__ == '__main__':
    unittest.main()