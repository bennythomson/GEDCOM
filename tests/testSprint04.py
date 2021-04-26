import unittest
import sqlite3
import sys
sys.path.append('../')
import classes
import Sprint04


class TestUserStory22(unittest.TestCase):

    def test01(self):
        individual1 = classes.Individual('I2', 'Marge /Bouvier/ ', 'F', '1980-03-19', 'F', None, None, 'F1')
        individual2 = classes.Individual('I2', 'Buck /Simpson/ ', 'F', '1980-03-19', 'F', None, None, 'F1')

        Sprint04.unique_ids(individual1.id)
        self.assertEqual(Sprint04.unique_ids(individual2.id), individual2.id)

class TestUserStory23(unittest.TestCase):

    def test01(self):
        individual1 = classes.Individual('I1', 'Marge /Bouvier/ ', 'F', '1980-03-19', 'F', None, None, 'F1')
        individual2 = classes.Individual('I2', 'Marge /Bouvier/ ', 'F', '1980-03-19', 'F', None, None, 'F4')

        Sprint04.unique_name_and_birthday(individual1)
        self.assertEqual(Sprint04.unique_name_and_birthday(individual2), individual2.id)

class TestUserStory24(unittest.TestCase):

    def test01(self):
        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'F', '1920-01-01', None, 'F1')
        children = classes.Individual('I1', 'Homer Simpson', 'M', '2022-01-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '2020-01-01', 'T', '2021-01-1', 'I1', 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [children])
        fam2 = classes.Family('F2', '2010-09-08', None, husband, wife, [children])


        self.assertIsNone(Sprint04.unique_family(fam1))
        self.assertEqual(Sprint04.unique_family(fam2), fam2.id)



class TestUserStory25(unittest.TestCase):

    def test01(self):
        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'F', '1920-01-01', None, 'F1')
        child = classes.Individual('I1', 'Bart Simpson', 'M', '2022-01-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '2020-01-01', 'T', '2021-01-1', 'I1', 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [child, child])


        self.assertEqual(Sprint04.unique_names_in_family(fam1), fam1.id)

class TestUserStory14(unittest.TestCase):

    def test01(self):
        #US 14 - No more than five siblings should be born at the same time
        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'F', '1920-01-01', 'I1', 'F1')
        child = classes.Individual('I1', 'Bart Simpson', 'M', '2022-01-01', 'T', None, None, None)
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '2020-01-01', 'T', '2021-01-1', 'I1', 'F1')

        # passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [child, child, child, child, child])

        self.assertEqual(Sprint04.multiple_births_in_family(fam1), fam1.id)

class TestUserStory21(unittest.TestCase):

    def test01(self):
        #US 21 - Husband in family should be male and wife in family should be female
        wife = classes.Individual('I2', 'Marge Simpson', 'M', '1900-01-01', 'F', '1920-01-01', 'I1', 'F1')
        child = classes.Individual('I1', 'Bart Simpson', 'M', '2022-01-01', 'T', None, None, None)
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '2020-01-01', 'T', '2021-01-1', 'I1', 'F1')

        # passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-09-08', None, husband, wife, [child, child, child, child, child])

        self.assertEqual(Sprint04.correct_gender_role(fam1), fam1.id)

if __name__ == '__main__':
    unittest.main()
