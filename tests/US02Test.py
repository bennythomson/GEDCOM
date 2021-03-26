import unittest
import sys
import paul
sys.path.append('../')

# Individual's Attributes: ID, Name, sex, birth, aliveBoolean, death, child, spouse
# Family Attributes: ID, Marriage date, divorce date, husband ID, wife ID, children
class US02Test(unittest.TestCase):

    def test01_Valid(self):
        # If birth date is after marriage date
        individual = paul.Individual('I2', 'Marge /Bouvier/ ', 'F', '1980-03-19', 'F', None, None, 'F1')
        family = paul.Family('F1', '1976-04-07', None, 'I1', 'I2', 'I7')
        self.assertTrue(paul.birth_after_marriage(individual, family), 'I5')

    def test02_Invalid(self):
        # If birth date is after marriage date
        individual = paul.Individual('I2', 'Marge /Bouvier/ ', 'F', '1980-03-19', 'F', None, None, 'F1')
        family = paul.Family('F1', '1976-04-07', None, 'I1', 'I2', 'I7')
        self.assertNotEqual(paul.birth_after_marriage(individual, family), 'I5')

    def test03_NoMarriage(self):
        # If marriage never happens
        individual = paul.Individual('I2', 'Marge /Bouvier/ ', 'F', '1956-03-19', 'F', None, None, 'F1')
        family = paul.Family('F1', None, None, 'I1', 'I2', 'I7')
        self.assertFalse(paul.birth_after_marriage(individual, family), 'I5')

    def test04_NoBirth(self):
        # If birth never happens
        individual = paul.Individual('I2', 'Marge /Bouvier/ ', 'F', None, 'F', None, None, 'F1')
        family = paul.Family('F1', '1976-04-07', None, 'I1', 'I2', 'I7')
        self.assertIsNot(paul.birth_after_marriage(individual, family), 'I5')

    def test05_NoArgs(self):
        # if both arg are empty
        individual = None
        family = None
        self.assertIsNone(paul.birth_after_marriage(individual, family), 'I5')


if __name__ == '__main__':
    unittest.main()