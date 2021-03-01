import unittest
import sqlite3
import sys

sys.path.append('../')
import mc


class TestUS06(unittest.TestCase):
    # this will test to make sure if person I know is divorced post death is true
    def test_CorrectAnswer(self):
        connection = sqlite3.connect("./family.db")
        lst = mc.divorce_after_death(connection)
        self.assertEqual(['I5'], lst)

    def test_TrueValue(self):
        connection2 = sqlite3.connect("./family.db")
        lst2 = mc.divorce_after_death(connection2)
        self.assertTrue(['I5'], lst2)

    def test_None(self):
        connection3 = sqlite3.connect("./family.db")
        lst3 = mc.divorce_after_death(connection3)
        self.assertIsNone(['DEAT'], lst3)

if __name__ == '__main__':
    unittest.main()



