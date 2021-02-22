import sys
import sqlite3
from sqlite3 import Error
import datetime
from dateutil.relativedelta import relativedelta


print("\nSSW 555: Project 02")
print("\nRun by MariaCristina Todaro\n")


print('Please specify GEDCOM file: ')
#filename = input()

gedcomfile = open("simpson_family.ged","r")

#gedcomfile = open('testged.ged', 'r')
#sys.stdout = open("Project02Results.txt", "w")


supported_tags = [ "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE",
                  "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
caution = ["INDI", "FAM"]

print("bruh")

def init_db(db_file, sql_filename):
    #Creates and connects to the local SQLite Database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
   


    cursor = conn.cursor()


    sql = 'DELETE FROM individuals'
    cursor.execute(sql)

    sql = 'DELETE FROM families'
    cursor.execute(sql)

    sql_file = open(sql_filename)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    
    return conn

def parse_data(conn):

    current_line = 0

    current_id = None
    record_type = None

    for line in iter(gedcomfile):



        level = line[:1]


       
        splitting = line.split()
        # print(splitting)
        indices = [1]
        tag = [splitting[index] for index in indices]
        # print(tag)
        arguments = line[6:]
        argue = arguments.split()



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

        print("<--", level, "|", tag, "|", valid, "|", argue,"\n")

        args_string = ""
        for arg in argue:
            args_string += arg + " "
        args_string.strip("@")

        if int(level)==0 and tag=="INDI":
            #add new individual

            current_id = argue.strip("@")
            print("current " + argue)
            record_type = "INDI"

            query = '''
                        INSERT INTO individuals(ID) VALUES(?)
                    '''
            cur = conn.cursor()
            cur.execute(query, (current_id,))
            conn.commit()


        if int(level) > 0 and record_type=="INDI":
            #update the indivual table
            cur = conn.cursor()
            if tag[0] == "NAME":

                query = "UPDATE individuals SET NAME = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))
            elif tag[0] == "SEX":
                query = "UPDATE individuals SET SEX = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))
            elif tag[0] == "BIRT":
                data = next(gedcomfile).split()[2:]
                
                data_string = ""
                for i in data:
                    data_string += i + " "
               
                query = "UPDATE individuals SET BIRT = ? WHERE ID = ?"

                date_time_obj = datetime.datetime.strptime(data_string, '%d %b %Y ')

                age = relativedelta(date_time_obj, datetime.datetime.now())
                
                cur.execute(query,(data_string,current_id))
                print(age.year)

            elif tag[0] == "DEAT":
                data = next(gedcomfile).split()[2:]
                
                data_string = ""
                for i in data:
                    data_string += i + " "
               
                query = "UPDATE individuals SET ALIVE='F', DEAT = ? WHERE ID = ?"

                
                cur.execute(query,(data_string,current_id))

            elif tag[0] == "FAMS":
                query = "UPDATE individuals SET SPOUSE = ? WHERE ID = ?"
                cur.execute(query,(args_string.strip("@"),current_id))

            elif tag[0] == "FAMC":
                query = "UPDATE individuals SET CHIL = ? WHERE ID = ?"
                cur.execute(query,(args_string.strip("@"),current_id))

            else: 
                pass
           

        ## ADD NEW FAMILY
        if int(level)==0 and tag=="FAM":
            #add new individual

            current_id = argue.strip("@")
            #print("current " + argue)
            record_type = "FAM"

            query = '''INSERT INTO families(ID) VALUES(?)'''
            cur = conn.cursor()
            cur.execute(query, (current_id,))
            conn.commit()
        

        if int(level) > 0 and record_type=="FAM":
            #Update each family row by row
            cur = conn.cursor()

            if tag[0] == "HUSB":

                query = "UPDATE families SET husband_id = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))

            elif tag[0] == "WIFE":
                query = "UPDATE families SET wife_id = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))

            elif tag[0] == "CHIL":
                query = "UPDATE families SET children = ? WHERE ID = ?"
                cur.execute(query,(args_string,current_id))
            
        
  

    
    #sys.stdout.close()



conn = init_db("./family.db","./init_db.sql")
parse_data(conn)
