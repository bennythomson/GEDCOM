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




def birth_before_parents_marriage(family=None):
    '''takes in a Family object, then gets the Individual object for each child in the family.
    Then, returns a list of all children who were born before their parents were married (the horror!)'''

    if(family != None):
        if (family.marriage == None):
            return None
        if(family.children != None):
            marriage_date = format_date(family.marriage)

            #This gets the list of children from the family, and converts them into an Individual object
            children = family.get_children()
            for child in children:
                if format_date(child.birthday) <= marriage_date:
                    print("Error US08: Family " + family.id + "  Your parents were scandalous and had a child out of wed lock")
                    return family.id
    return None

#TODO - similar as above method
def birth_before_parents_death(family=None):
    '''Takes in family object. Then, get the Individual for both parents and each child. Then, loop thru
    all the children and compare their birthdays with the husband and wife birthday'''
    if family != None:
        if family.marriage == None:
            return None
        if family.children != None:
            children = family.get_children()
            mom = family.wife
            dad = family.husband

            if mom.death is None or dad.death is None:
                return None

            for child in children:
                kiddo = format_date(child.birthday)
                if kiddo >= format_date(mom.death):
                    print("Error US09: Child", child.id, "was born after mother's death")
                    return child.id
                if format_date(dad.death) - relativedelta(days=273) >= kiddo:
                    print("Error US09: Child", child.id, "was born more than 9 months before father's death")
                    return child.id

def marriage_after_14(family=None):
    '''returns an error if an individual was married before they were 14
    Takes in a Family object, and gets the Individual corresponding to the Husband and Wife.
    From there, we can compare each person's birthday and the date of their marriage'''

    if(family is None or family.marriage is None):

        return None

    marriage_date = format_date(family.marriage)
    husband = family.husband
    wife = family.wife

    husband_birthday = format_date(husband.birthday)
    wife_birthday = format_date(wife.birthday)

    if((husband_birthday + relativedelta(years=14)) >= marriage_date and (wife_birthday + relativedelta(years=14)) >= marriage_date):
        print("Error US10: Family " + family.id + " husband " + husband.id + " and wife " + wife.id + " were married before 14")
        return (husband.id, wife.id)

    if((husband_birthday + relativedelta(years=14)) >= marriage_date):
        print("Error US10: Family " + family.id + " husband " + husband.id + " was married before 14")
        return husband.id

    if((wife_birthday + relativedelta(years=14)) >= marriage_date):
        print("Error US10: Family " + family.id + " wife " + wife.id + " was married before 14")
        return wife.id

    return None

def no_bigamy(family1 = None, family2  = None):

    if(family1 == None or family2 == None):
        return None
    if(family1.id == family2.id):
        return None

    if(family1.husband == family2.husband or family1.wife == family2.wife):
        #if(format_date(family2.divorce) > format_date(family1.marriage) or format_date(family1.divorce) > format_date(family2.marriage)):
        print("US11:  bigamy between " +family1.id + " and " + family2.id)
        return (family1, family2)
    return None

def parents_not_too_old(family = None):
    if(family is None):
        return None
    if family.wife is None or family.husband is None:
        return None
    #print(family.wife)
    wife = family.wife
    husband = family.husband
    children = family.get_children() #this is a list of Individual objects

    if wife.birthday is None or husband.birthday is None:
        return None

    wife_birth_date = format_date(wife.birthday)

    if(wife.death is None):
        wife_end_date = date.today()
    else:
        wife_end_date = format_date(wife.death)

    if(husband.death is None):
        husband_end_date = date.today()
    else:
        husband_end_date = format_date(husband.death)

    wife_age = int((wife_end_date - wife_birth_date).days / 365)

    husband_birth_date = format_date(husband.birthday)
    husband_age = int((husband_end_date - husband_birth_date).days / 365)

    for child in children:

        child_birth_date = format_date(child.birthday)

        if (-(wife_birth_date - child_birth_date).days /365 >= 60 or (husband_birth_date - child_birth_date).days / 365 >= 80):
            print("Error US12: " + child.id +" parents are old")
            return child.id
    return None

#TODO: User story 13
def sibling_spacing(family= None):
    if family != None:
        if family.marriage == None:
            return None
        if family.children != None:
            children = family.children
            for child in children:
                child_1 = format_date(child.birthday)
                child_2 = format_date(child.birthday)
                if int((child_1 - child_2).days) <= 243:
                    print("Error US13: Siblings from family", family.id, "are less than 8 months apart")
                    return family.id
                if int((child_1 - child_2).days) > 2 or int((child_1 - child_2).days) < 243:
                    print("Error US13: Twins from family", family.id, "are more than 2 days apart")
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
        parents_not_too_old(fam_obj)
        marriage_after_14(fam_obj)
        birth_before_parents_marriage(fam_obj)
        birth_before_parents_death(fam_obj)

        #loop thru families again for bigamy method
        for family2 in families:

            fam_obj2 = classes.Family(family2[0], family2[1], family2[2],family2[3],family2[4],family2[5],)
            no_bigamy(fam_obj, fam_obj2)
