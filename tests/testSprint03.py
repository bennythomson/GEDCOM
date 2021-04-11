import unittest
import sqlite3
import sys
sys.path.append('../')
import classes
import Sprint03


class TestUserStory29(unittest.TestCase):

    def test01(self):
        '''User story 29 - list deceased '''


        person = classes.Individual('I1', 'Marge Simpson', 'F', '1900-01-01', 'F', '1920-01-01', None, 'F1')

        self.assertEqual(Sprint03.list_deceased(person), 'I1')


class TestUserStory35(unittest.TestCase):

    def test01(self):
        '''User story 35 - recent births '''
        person = classes.Individual('I1', 'Marge Simpson', 'F', '2021-04-09', 'T', None, None, 'F1')

        self.assertEqual(Sprint03.list_recent_births(person), 'I1')


class TestUserStory36(unittest.TestCase):

    def test01(self):
        '''User story 36 - recent deaths'''

        person = classes.Individual('I1', 'Marge Simpson', 'F', '1980-04-09', 'T', '2021-04-09', None, 'F1')

        self.assertEqual(Sprint03.list_recent_deceased(person), 'I1')

class TestUserStory38(unittest.TestCase):

    def test01(self):
        '''User story 38 - upcomining birthdays'''

        person = classes.Individual('I1', 'Marge Simpson', 'F', '1980-04-20', 'T', '2040-04-09', None, 'F1')

        self.assertEqual(Sprint03.list_upcoming_birthdays(person), 'I1')

class TestUserStory39(unittest.TestCase):

    def test01(self):
        '''User story 38 - upcoming anniversaries'''

        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'T', None, None, 'F1')
        children = classes.Individual('I1', 'Homer Simpson', 'M', '2000-01-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '1800-01-01', 'T', None, 'I1', 'F1')

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-04-15', None, husband, wife, [children])

        self.assertEqual(Sprint03.list_upcoming_anniversaries(fam1), 'F1')

class TestUserStory15(unittest.TestCase):

    def test01(self):
        '''User story 15 -  15 siblings'''

        wife = classes.Individual('I2', 'Marge Simpson', 'F', '1900-01-01', 'T', None, None, 'F1')
        husband = classes.Individual('I3', 'Abraham Simpson', 'M', '1800-01-01', 'T', None, 'I1', 'F1')

        children = []
        for i in range(0,16):
            kid = classes.Individual('I' + str(i), 'child'+str(i), 'M', '1900-01-01', 'T', None, None, 'F1')
            children.append(kid)

        #passing in objects as the husband and wife instead of their IDs
        fam1 = classes.Family('F1', '2010-04-15', None, husband, wife, children)

        self.assertEqual(Sprint03.fewer_than_15_siblings(fam1), 'F1')



if __name__ == '__main__':
    unittest.main()
