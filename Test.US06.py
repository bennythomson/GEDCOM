import unittest
import sys
sys.path.append('../')
import working_mc


class TestUS06(unittest.TestCase):
    def testCorrectCase1(self):
        # we will check the person we know is divorced post death as a test case
        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Individual('I5', 'Mona /Olsen/', 'F', '1929-03-15', 'F', '2007-07-06', 'None', 'F2')
        # Family: ID Marriage Date Divorce Date Husband Wife Child
        family = working_mc.Family('F2', '2010-09-08', '2011-05-06', 'I3', 'I5', 'I1')
        # test to see if correct case runs from user story
        self.assertEqual(working_mc.divorce_after_death(individual, family), 'I5')

    def testIncorrectCase2(self):
        # we will check if an error occurs when the death death is greater than divorce date
        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Individual('I5', 'Mona /Olsen/', 'F', '1929-03-15', 'F', '2015-07-06', 'None', 'F2')
        # Family: ID Marriage Date Divorce Date Husband Wife Child
        family = working_mc.Family('F2', '2010-09-08', '2011-05-06', 'I3', 'I5', 'I1')
        # test to see if correct case runs from user story
        self.assertNotEqual(working_mc.divorce_after_death(individual, family), 'I5')

    def testNoDivorce3(self):
        # this will test what happens if a divorce never happens
        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Individual('I5', 'Mona /Olsen/', 'F', '1929-03-15', 'F', '2007-07-06', 'None', 'F2')
        # Family: ID Marriage Date Divorce Date Husband Wife Child
        family = working_mc.Family('F2', '2010-09-08', None, 'I3', 'I5', 'I1')
        # test to see if correct case runs from user story
        self.assertFalse(working_mc.divorce_after_death(individual, family), 'I5')

    def testIsNot4(self):
        # this will test if the divorce is not after death
        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Individual('I5', 'Mona /Olsen/', 'F', '1929-03-15', 'F', '2007-07-06', 'None', 'F2')
        # Family: ID Marriage Date Divorce Date Husband Wife Child
        family = working_mc.Family('F2', '2010-09-08', '2005-05-06', 'I3', 'I5', 'I1')
        # test to see if correct case runs from user story
        self.assertIs(working_mc.divorce_after_death(individual, family), 'I5')

    def testIsNone5(self):
        # this will test if there is divorce post death
        # Individual: ID Name Sex Birth Alive Death Child Family in list
        individual = working_mc.Individual('I5', 'Mona /Olsen/', 'F', '1929-03-15', 'F', '2007-07-06', 'None', 'F2')
        # Family: ID Marriage Date Divorce Date Husband Wife Child
        family = working_mc.Family('F2', '2010-09-08', '2015-08-09', 'I3', 'I5', 'I1')
        # test to see if correct case runs from user story
        self.assertTrue(working_mc.divorce_after_death(individual, family), 'I5')

if __name__ == '__main__':
    unittest.main()



