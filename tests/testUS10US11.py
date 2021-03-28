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
        wife = classes.Individual('I2', 'Marge Bouiver', 'F', '1920-01-01', 'T', '1980-01-01', None, 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam = classes.Family('F1', '1905-01-01', None, husband, wife, None)
        

        self.assertEqual(Sprint02.marriage_after_14(fam), 'I1')

if __name__ == '__main__':
    unittest.main()
