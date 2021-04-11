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


def list_deceased(individual = None):

    '''List all people in a GEDCOM file who are dead'''

    if individual is None or individual.alive is None:
        return None

    if individual.alive == "F":
        print("US29: Individual " + individual.id + " is deceased.")
        return individual.id


def list_recent_deceased(individual = None):
    '''List all people in a GEDCOM file who died in the last 30 days'''

    if individual is None or individual.death is None:
        return None

    today = date.today()
    individual_death = format_date(individual.death)


    if (today - individual_death).days <= 30:

        print("US 36: Individual " + individual.id + " died in the last month.")
        return individual.id


def list_recent_births(individual = None):
    #User Story 35
    '''List all people in a GEDCOM file who were born in the last 30 days'''

    if individual is None or individual.birthday is None:
        return None

    today = date.today()
    individual_birthday = format_date(individual.birthday)


    if (today - individual_birthday).days <= 30:

        print("US 35: Individual " + individual.id + " is less than one month old.")
        return individual.id

def list_upcoming_anniversaries(family = None):
    '''User story 39: List all living couples in a GEDCOM file whose marriage anniversaries occur in the unext 30 days'''
    if family is None or family.marriage is None:
        return none


    today = date.today()
    parsed = format_date(family.marriage).replace(year=today.year)

# today < parsed <= 30 days from now
    if parsed >= today and parsed <= (today + timedelta(days=30)):
        print("US39: Anniversary Date of " + family.id + " is in the next month")
        return family.id

def list_upcoming_birthdays(individual = None):
    '''User story 38: List people whose birthday is within a month'''
    if individual is None or individual.birthday is None:
        return None


    today = date.today()
    parsed = format_date(individual.birthday).replace(year=today.year)

    if parsed >= today and parsed <= (today + timedelta(days=30)):
        print("US38:  Individual " + individual.id + "'s birthday is in the next month")
        return individual.id


def fewer_than_15_siblings(family = None):
    '''US15 cant be more than 15 children per family'''
    if family is None or not family.children:
        return None

    if(len(family.children) > 15):
        print("Error US15: More than 15 children in family " + family.id)
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
        fewer_than_15_siblings(fam_obj)
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
                list_deceased(indiv_obj)
                list_recent_deceased(indiv_obj)
                list_upcoming_birthdays(indiv_obj)
