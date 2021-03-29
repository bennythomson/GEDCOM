import unittest
import sqlite3
import sys
sys.path.append('../')
import classes
import Sprint02

class TestUserStory10(unittest.TestCase):
    '''make sure nobody gets married before the age of 14'''


    def test01(self):
        '''husband under 14'''
        '''Expect to return the husband's ID'''
        husband = classes.Individual('I1', 'Homer Simpson', 'M', '1900-01-01', 'T', '1980-01-01', None, 'F1')
        wife = classes.Individual('I2', 'Marge Bouiver', 'F', '1800-01-01', 'T', '1980-01-01', None, 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam = classes.Family('F1', '1905-01-01', None, husband, wife, None)


        self.assertEqual(Sprint02.marriage_after_14(fam), 'I1')

    def test02(self):
        '''wife under 14'''
        '''Expect to return the wife's ID'''
        husband = classes.Individual('I1', 'Homer Simpson', 'M', '1880-01-01', 'T', '1980-01-01', None, 'F1')
        wife = classes.Individual('I2', 'Marge Bouiver', 'F', '1901-01-01', 'T', '1980-01-01', None, 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam = classes.Family('F1', '1905-01-01', None, husband, wife, None)


        self.assertEqual(Sprint02.marriage_after_14(fam), 'I2')

    def test03(self):
        '''both over 14'''
        '''Expect to return None'''
        husband = classes.Individual('I1', 'Homer Simpson', 'M', '1900-01-01', 'T', '1980-01-01', None, 'F1')
        wife = classes.Individual('I2', 'Marge Bouiver', 'F', '1900-01-01', 'T', '1980-01-01', None, 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam = classes.Family('F1', '1960-01-01', None, husband, wife, None)


        self.assertEqual(Sprint02.marriage_after_14(fam), None)

class TestUserStory11(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
