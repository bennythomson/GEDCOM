import sys
import sqlite3
from sqlite3 import Error
import datetime
from dateutil.relativedelta import relativedelta
from prettytable import from_db_cursor

import Sprint01
import Sprint02
import Sprint03
import Sprint04
  
print('Please specify GEDCOM file: ')


#Open the file specified by the user

supported_tags = [ "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE",
                  "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
caution = ["INDI", "FAM"]


def init_db(db_file, sql_filename):

    #Creates and connects to the local SQLite Database
    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)



    cursor = conn.cursor()


    #Setup the tables using the local SQL file
    sql_file = open(sql_filename)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

    #Clears the database's tables

    sql = 'DELETE FROM individuals'
    cursor.execute(sql)

    sql = 'DELETE FROM families'
    cursor.execute(sql)


    return conn

def parse_data(conn, gedcomfile):


    current_line = 0

    current_id = None
    record_type = None

    #Goes line by line in the file and updates the Database
    for line in iter(gedcomfile):



        level = line[:1]



        splitting = line.split()
        # print(splitting)
        indices = [1]
        tag = [splitting[index] for index in indices]
        # print(tag)
        arguments = line[6:]
        argue = arguments.split()


        #Order the line's arguments so that theyre in a uniform location
        for word in argue:
            if word in caution:
                valid = "Y"
                splitting[1], splitting[2] = splitting[2], splitting[1]
                tag = splitting[1]
                argue = splitting[2]
            else:
                for word in tag:
                    if word in supported_tags:
                        valid = "Y"
                    else:
                        valid = "N"

        #Format the line's arguments
        args_string = ""
        for arg in argue:
            args_string += arg + " "
        args_string = args_string.replace("@","")



        #Check is the current line is level 0 and specifies a new individual
        if int(level)==0 and tag=="INDI":

            #Current_id allows the lines following the creation of this individual to refer to the same person
            #Current_id is only updated when a new individual or family is created
            current_id = argue.strip("@")
            current_id = current_id.strip()
            record_type = "INDI"

            #Creates a  new individual in the DB
            query = '''
                        INSERT INTO individuals(ID, ALIVE) VALUES(?, 'T')
                    '''
            cur = conn.cursor()
            cur.execute(query, (current_id,))
            conn.commit()


        #Now, we're looking to see if we can update a particular individual

        #Ensure that the level is greater than 0 (implying these lines belong to the previously defined individual)
        if int(level) > 0 and record_type=="INDI":
            #update the indivual table
            cur = conn.cursor()

            #Now we check for each tag, and then update the row with the current line's arguments

            if tag[0] == "NAME":
                query = "UPDATE individuals SET NAME = ? WHERE ID = ?"
                cur.execute(query, (args_string, current_id))
            elif tag[0] == "SEX":
                query = "UPDATE individuals SET SEX = ? WHERE ID = ?"
                cur.execute(query, (args_string, current_id))

            elif tag[0] == "BIRT":
                #This wonderful file format stores the date information on the next line, so we have to peek ahead to get the date of the indivual's birth or death
                data = next(gedcomfile).split()[2:]

                data_string = ""
                for i in data:
                    data_string += i + " "
                birth_date = datetime.datetime.strptime(data_string, '%d %b %Y ').date()

                query = "UPDATE individuals SET BIRT = ? WHERE ID = ?"

                cur.execute(query, (birth_date, current_id))


            elif tag[0] == "DEAT":
                data = next(gedcomfile).split()[2:]

                data_string = ""
                for i in data:
                    data_string += i + " "

                death_date = datetime.datetime.strptime(data_string, '%d %b %Y ').date()

                query = "UPDATE individuals SET ALIVE='F', DEAT = ? WHERE ID = ?"


                cur.execute(query,(death_date,current_id))

            elif tag[0] == "FAMS":
                query = "UPDATE individuals SET SPOUSE = ? WHERE ID = ?"
                args_string = args_string.replace('@', '')
                #print(args_string)
                cur.execute(query, (args_string, current_id))

            elif tag[0] == "FAMC":
                query = "UPDATE individuals SET CHIL = ? WHERE ID = ?"
                args_string = args_string.replace('@', '')
                cur.execute(query, (args_string, current_id))

            else:
                pass
            conn.commit()



        ## ADD NEW FAMILY, this works the same way as adding/updating an individual
        if int(level) == 0 and tag == "FAM":


            current_id = argue.strip("@")
            record_type = "FAM"

            query = '''INSERT INTO families(ID) VALUES(?)'''
            cur = conn.cursor()
            cur.execute(query, (current_id,))
            conn.commit()

        if int(level) > 0 and record_type=="FAM":
            # print(line)
            # Update each family row by row
            cur = conn.cursor()

            if tag[0] == "HUSB":

                query = "UPDATE families SET husband_id = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))

                conn.commit()
            elif tag[0] == "WIFE":
                query = "UPDATE families SET wife_id = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))
                conn.commit()

            elif tag[0] == "CHIL":


                cur.execute("SELECT children FROM families WHERE ID = ? ",(str(current_id),))
                existing_data = cur.fetchall()

                all_children = ""
                for child in existing_data:
                    if child[0] is not None:
                        all_children += child[0] + args_string + ","
                    else:
                        all_children += args_string + ","


                query = "UPDATE families SET children = ? WHERE ID = ?"
                cur.execute(query,(all_children,current_id))
                conn.commit()

            elif tag[0] == "MARR":
                data = next(gedcomfile).split()[2:]

                data_string = ""
                for i in data:
                    data_string += i + " "

                marriage_date = datetime.datetime.strptime(data_string, '%d %b %Y ').date()

                query = "UPDATE families SET marriage_date = ? WHERE ID = ?"
                cur.execute(query,(marriage_date,current_id))
                conn.commit()

            elif tag[0] == "DIV":
                data = next(gedcomfile).split()[2:]

                data_string = ""
                for i in data:
                    data_string += i + " "

                divorce_date = datetime.datetime.strptime(data_string, '%d %b %Y ').date()
                query = "UPDATE families SET divorce_date = ? WHERE ID = ?"
                cur.execute(query,(divorce_date,current_id))
                conn.commit()
            else:
                pass
            conn.commit()


def validate_output(conn):
    #runs tests to validate the output
    Sprint01.user_stories(conn)
    Sprint02.user_stories(conn)
    Sprint03.user_stories(conn)
    Sprint04.user_stories(conn)



if __name__ == '__main__':

    filename = input()

    conn = init_db("./family.db","./init_db.sql")
    file = open(filename,"r")
    parse_data(conn, file)

    connection = sqlite3.connect("./family.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM individuals")
    mytable = from_db_cursor(cursor)

    print(mytable)

    cursor.execute("SELECT * FROM families")
    mytable = from_db_cursor(cursor)

    print(mytable)

    validate_output(conn)
