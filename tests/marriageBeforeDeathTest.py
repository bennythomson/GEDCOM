import unittest
import sqlite3
import sys
sys.path.append('../')
import ben
class TestUserStory05(unittest.TestCase):

    def test01(self):

        #in order:
        #ID, Name, sex, birth, alive?, child, family
        ind = ('I2', 'Marge /Bouvier/ ', 'F ', '1956-03-19', 'F', '1960-03-19', None, 'F1 ')

        #ID, marriage, divorce, husband, wife, children
        fam = ('F3', '1970-08-03', '1970-08-03', 'I2', 'I3', None)


        self.assertEqual(ben.marriage_after_death(ind, fam), 'I2')

    def test02(self):

        self.assertIsNone(ben.marriage_after_death(None, None))

    def test03(self):

        #in order:
        #ID, Name, sex, birth, alive?, child, family
        ind = ('I2', 'Marge /Bouvier/ ', 'F ', '1956-03-19', 'F', '2000-03-19', None, 'F1 ')

        #ID, marriage, divorce, husband, wife, children
        fam = ('F3', '1970-08-03', '1970-08-03', 'I2', 'I3', None)


        self.assertEqual(ben.marriage_after_death(ind, fam), None)

    def test04(self):

        #in order:
        #ID, Name, sex, birth, alive?, child, family
        ind = ('I2', 'Marge /Bouvier/ ', 'F ', '1956-03-19', 'F', '2000-03-19', None, 'F1 ')

        #ID, marriage, divorce, husband, wife, children
        fam = ('F3', '1970-08-03', None, 'I2', 'I3', None)


        self.assertEqual(ben.marriage_after_death(ind, fam), None)

    def test05(self):

        #in order:
        #ID, Name, sex, birth, alive?, child, family
        ind = ('I2', 'Marge /Bouvier/ ', 'F ', None, 'F', '2000-01-01', None, 'F1 ')

        #ID, marriage, divorce, husband, wife, children
        fam = ('F3', '2000-01-01', '2000-01-01', 'I2', 'I3', None)


        self.assertEqual(ben.marriage_after_death(ind, fam), 'I2')



if __name__ == '__main__':
    unittest.main()
