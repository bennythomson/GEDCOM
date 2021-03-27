import datetime
import classes
import sqlite3
from datetime import date


def format_date(date_str):
    #takes in a string representing a date in Y-m-d format and returns a datetime object

    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()




def birth_before_parents_marriage(family=None):
    '''takes in a Family object, then gets the Individual object for each child in the family.
    Then, returns a list of all children who were born before their parents were married (the horror!)'''

    if(family != None):
        if (family.marriage == None):
            return None
        if(family.children != None):
            marriage_date = format_date(family.marriage)
            marriage_date = format_date(family.marriage)

            #This gets the list of children from the family, and converts them into an Individual object
            children = map(family.get_indiv, family.get_children())
            for child in children:
                if child.birthday <= marriage_date:
                    print("Error US08: Family " + family.id + "  Your parents were scandalous and had a child out of wed lock")


#TODO
def birth_before_parents_death(family=None):
    '''Takes in family object. Then, get the Individual for both parents and each child. Then, loop thru
    all the children and compare their birthdays with the husband and wife birthday'''
    if (individual != None and family != None):
        if (family.marriage == None):
            return None
        if (family.children != None):

            marriage_date = format_date(family.marriage)

            children = map(family.get_indiv, family.get_children())
            for child in children:
                if child.birthday <= marriage_date:
                    print("Error US08: Family " + family.id + "  Your parents were scandalous and had a child out of wed lock")

def marriage_after_14(family=None):
    '''returns an error if an individual was married before they were 14
    Takes in a Family object, and gets the Individual corresponding to the Husband and Wife.
    From there, we can compare each person's birthday and the date of their marriage'''

    if(family != None or family.marriage is None):
        return None

    marriage_date = format_date(family.marriage)
    husband = family.get_indiv(family.husband)
    wife = family.get_indiv(family.wife)

    husband_birthday = format_date(husband.birthday)
    wife_birthday = format_date(wife.birthday)

    if((husband_birthday + relativedelta(years=14)) <= marriage_date):
        print("Error US10: Family " + family.id + " husband " + husband.id + " was married before 14")
        return husband.id

    if((wife_birthday + relativedelta(years=14)) <= marriage_date):
        print("Error US10: Family " + family.id + " wife " + wife.id + " was married before 14")
        return husband.id

    return None

def no_bigamy(family1 = None, family2  = None):

    if(family1 == None or family2 == None):
        return None

    if(family1.husband == family2.husband or family1.wife == family2.wife):
        if(format_date(family2.divorce) > format_date(family1.marriage) or format_date(family1.divorce) > format_date(family2.marriage)):
            print("US11:  bigamy " +family1.id + " and " + family2.id)
            return (family1, family2)
    return None

def parents_not_too_old(family = None):
    if(family == None):
        return None
    wife = get_indiv(family.wife)
    husband = get_indiv(family.husband)
    children = get_indiv(family.children)

    if (wife != None or husband != None or child != None):
        wife_death_date = format_date(wife.death)
        wife_birth_date = format_date(wife.birthday)
        wife_age = int((wife_death_date - wife_birth_date).days / 365)

        husband_death_date = format_date(husband.death)
        husband_birth_date = format_date(husband.birthday)
        husband_age = int((husband_death_date - husband_birth_date).days / 365)

        child_birth_date = format_date(child.birthday)

        if ((wife_birth_date - child_birth_date).days /365 >= 60 or (husband_birth_date - child_birth_date).days / 365 >= 80):
            print("Error US12: " + child.id +" parents are ollllldddddddd")
            return child.id
    return None

#TODO: User story 13

def user_stories(conn):

    '''executes all of the user stories contained in this module'''

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    familes = cur.fetchall()

    for family in familes:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = classes.Family(family[0], family[1], family[2],family[3],family[4],family[5],)
        parents_not_too_old(fam_obj)

        #loop thru families again for bigamy method
        for family2 in families:
            fam_obj2 = classes.Family(family2[0], family2[1], family2[2],family2[3],family2[4],family2[5],)
            no_bigamy(fam_obj, fam_obj2)



        #loop through each individual in the family
        for indiv in list(family[3:4]) + fam_obj.get_children():
            #print("family children: ")
            #print(fam_obj.get_children())
            if indiv != None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()
            #    print(indiv_result)
                indiv_obj = classes.Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

                birth_before_parents_marriage(fam_obj)
                birth_before_parents_death(fam_obj)
                marriage_after_14(indiv_obj, fam_obj)
