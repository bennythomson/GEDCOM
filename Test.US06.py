import unittest
import sqlite3
import sys

sys.path.append('../')
import mc


class TestUS06(unittest.TestCase):
    # this will test to make sure if person I know is divorced post death is true
    def test_TrueValue(self):
        connection2 = sqlite3.connect("./family.db")
        lst2 = mc.divorce_after_death(connection2)
        self.assertTrue(['I5'], lst2)

    def test_NotNone(self):
        connection = sqlite3.connect("./family.db")
        lst = mc.divorce_after_death(connection)
        self.assertIsNotNone(['I5'], lst)

    def test_WrongValue(self):
        connection = sqlite3.connect("./family.db")
        lst3 = mc.divorce_after_death(connection)
        self.assertNotEqual(['I4'],lst3)

    def test_CorrectAnswer(self):
        connection = sqlite3.connect("./family.db")
        lst4 = mc.divorce_after_death(connection)
        self.assertIsNot(['I5'], lst4)


if __name__ == '__main__':
    unittest.main()



