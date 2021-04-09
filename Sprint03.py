import datetime
import classes
import sqlite3
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def format_date(date_str):
    #takes in a string representing a date in Y-m-d format and returns a datetime object
    if date_str is None:
        return None
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()



def list_recent_births(individual = None):
    #User Story 35
    '''List all people in a GEDCOM file who were born in the last 30 days'''

    if individual is None or individual.birthday is None:
        return None

    today = date.today()
    individual_birthday = format_date(individual.birthday)


    if (today - individual_birthday).days <= 30:

        print("Individual " + individual.id + " is less than one month old.")
        return individual.id

def list_upcoming_anniversaries(family = None):
    '''User story 39: List all living couples in a GEDCOM file whose marriage anniversaries occur in the unext 30 days'''
    if family is None or family.marriage is None:
        return none


    today = date.today()
    parsed = format_date(family.marriage).replace(year=today.year)


    if (parsed - timedelta(days=30)) <= today:
        print("Anniversary Date of " + family.id + " is in the next month")
        return family.id




def user_stories(conn):

    '''executes all of the user stories contained in this module'''

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    families = cur.fetchall()

    for family in families:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = classes.Family(family[0], family[1], family[2],family[3],family[4],family[5],)
        list_upcoming_anniversaries(fam_obj)
        #New loop for each person in the file
        for indiv in list(family[3:5]) + fam_obj.get_children_ids():

            if indiv != None:

                indiv = indiv.strip()
                new_cur = conn.cursor()
                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()
            #    print(indiv_result)
                indiv_obj = classes.Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

                #now we have the individual
                list_recent_births(indiv_obj)
