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
    '''no bigamy'''
    def test01(self):
        husband = classes.Individual('I1', 'Homer Simpson', 'M', '1900-01-01', 'T', '1980-01-01', None, 'F1')
        wife = classes.Individual('I2', 'Marge Bouiver', 'F', '1900-01-01', 'T', '1980-01-01', None, 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '1960-01-01', None, husband, wife, None)
        fam2 = classes.Family('F2', '1980-01-01', None, husband, wife, None)

        self.assertEqual(Sprint02.no_bigamy(fam1, fam2), (fam1, fam2))

class TestUserStory12(unittest.TestCase):

    def test01(self):
        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'T', '2020-01-01', None, 'F1')
        children = classes.Individual('I1', 'Homer Simpson', 'M', '2000-01-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '1800-01-01', 'T', '1980-01-01', 'I1', 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [children])

        self.assertEqual(Sprint02.parents_not_too_old(fam1),'I1')

class TestUserStory13(unittest.TestCase):

    def test01(self):
        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'T', '2020-01-01', None, 'F1')
        children_1 = classes.Individual('I1', 'Homer Simpson', 'M', '2000-01-01', 'T', None, None, 'F1')
        children_2 = classes.Individual('I4', 'Alex Simpson', 'M', '2000-05-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '1800-01-01', 'T', '1980-01-01', 'I1, I4', 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [children_1, children_2])

        self.assertEqual(Sprint02.sibling_spacing(fam1), 'F1')



if __name__ == '__main__':
    unittest.main()
