import unittest
import sqlite3
import sys
sys.path.append('../')
import ben
import CS555
class TestUserStory05(unittest.TestCase):

    def test01(self):
        
        conn = None

        try:
            conn = sqlite3.connect(':memory:')

        except Error as e:
            print(e)


        cursor = conn.cursor()


        #Setup the tables using the local SQL file
        sql_file = open("../init_db.sql")
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)

        #Clears the database's tables

        sql = 'DELETE FROM individuals'
        cursor.execute(sql)

        sql = 'DELETE FROM families'
        cursor.execute(sql)




        CS555.parse_data(conn, test_ged.splitlines())

        lst = ben.marriage_before_death(connection)
        self.assertEqual(['I5'], lst)


if __name__ == '__main__':
    unittest.main()
