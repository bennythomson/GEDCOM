import unittest
import sqlite3
import sys
sys.path.append('../')
import ben

class TestUserStory05(unittest.TestCase):

    def testCorrectFamily(self):
        connection = sqlite3.connect("../family.db")

        lst = ben.marriage_before_death(connection)
        self.assertEqual(['I5'], lst)


if __name__ == '__main__':
    unittest.main()
