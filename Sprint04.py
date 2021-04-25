import datetime
import classes
import sqlite3
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta

list_of_ids = []

list_of_individuals = []

list_of_families = []

def format_date(date_str):
    #takes in a string representing a date in Y-m-d format and returns a datetime object
    if date_str is None:
        return None
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def unique_ids(ID):
    '''User Story 22: ensures that all individual and family IDs are unique'''
    if ID is None:
        return None

    if ID in list_of_ids:
        #ID has been seen before
        print("Error US22: ID " + ID + " is not unique.")
        return ID
    else:
        list_of_ids.append(ID)


def unique_name_and_birthday(individual = None):

    '''User Story 23 - ensures that No more than one individual with the same name and birth date should appear in a GEDCOM file'''

    if individual is None:
        return None

    list_of_individuals.append(individual)
    for individual_checked in list_of_individuals:

        if individual_checked.id != individual.id:
            if individual_checked.name == individual.name and individual_checked.birthday == individual.birthday:
                #error - duplicate info
                print("Error US 23: " + individual_checked.id + " and " + individual.id + " have the same name and birthday")
                return individual.id



    return None

def unique_family(family = None):
    '''makes sure no duplicate families exist'''
    if family is None:
        return None

    list_of_families.append(family)
    for fam in list_of_families:
        if fam.id != family.id:
            if fam.husband.name == family.husband.name and fam.wife.name == family.wife.name and fam.marriage == family.marriage:
                #error - duplicate info
                print("Error US 24: " + fam.id + " and " + family.id + " have the same name and birthday")
                return family.id


    return None

def unique_names_in_family(family = None):
    '''US 25 - No more than one child with the same name and birth date should appear in a family'''
    if family is None or family.children is None:
        return None


    family_children = family.children

    if not isinstance(family_children[0], classes.Individual):
        family_children = family.get_children()

    for child in family_children:

        for child2 in family_children:

            if child.name == child2.name and child.birthday == child2.birthday:
                print("Error US25: Child " + child.id + " and " + child2.id + " have the same name and birthday")
                return family.id
    return None


def user_stories(conn):

    '''executes all of the user stories contained in this module'''

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    families = cur.fetchall()

    for family in families:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = classes.Family(family[0], family[1], family[2],family[3],family[4],family[5],)
        unique_family(fam_obj)
        unique_names_in_family(fam_obj)
        #New loop for each person in the file
        for indiv in list(family[3:5]) + fam_obj.get_children_ids():

            if indiv != None:

                indiv = indiv.strip()
                new_cur = conn.cursor()
                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()
            #    print(indiv_result)
                indiv_obj = classes.Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])
                unique_name_and_birthday(indiv_obj)
