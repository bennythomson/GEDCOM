import datetime
import sqlite3
from datetime import date

class Individual:

    def __init__(self, id, name, sex, birthday, alive, death, children, spouse):

        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.alive = alive
        self.death = death
        self.children = children
        self.spouse = spouse

class Family:
    def __init__(self, id, marriage, divorce, husband, wife, children):
        #ID, marriage, divorce, husband, wife, children
        self.id = id
        self.marriage = marriage
        self.divorce = divorce
        self.husband = husband
        self.wife = wife
        self.children = children

def format_date(date_str):
    #takes in a string repreenting a date in Y-m-d format and returns a datetime object
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def get_indiv(ID):
    #takes I1
    connection = sqlite3.connect("./family.db")
    cur = connection.cursor()
    # Query all familes in database
    cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(ID),))
    indiv_result = cur.fetchall()

    indiv_obj = Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3],
                           indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

    return indiv_obj



def birth_before_parents_marriage(individual=None, family=None):
    if(individual != None and family != None):
        if (family.marriage == None):
            return None
        if(family.children != None):
            birth_date = format_date(individual.birthday)
            marriage_date = format_date(family.marriage)
            child_person = individual.id

            if child_person == family.children:

               # print("Error US08:", child_person, "is not an offspring of", family.id)
                if birth_date <= marriage_date:
                    print("Error US08: " + individual.id +"  Your parents were scandalous and had a child out of wed lock")


def birth_before_parents_death(individual=None, family=None):
    if (individual != None and family != None):
        if (family.marriage == None):
            return None
        if (family.children != None):
            birth_date = format_date(individual.birthday)
            marriage_date = format_date(family.marriage)
            child_person = individual.id

            if child_person == family.children:

                # print("Error US08:", child_person, "is not an offspring of", family.id)
                if birth_date <= marriage_date:
                    print("Error US08: " + individual.id + "  Your parents were scandalous and had a child out of wed lock")

def marriage_after_14(individual=None, family=None):
    #dont fear the reaper....


    '''This method returns the ID of the individual if their marriage date occurs
    after their death date'''
    if(individual != None and family != None):

        if(individual.birthday == None or family.marriage == None):
            return None

        marriage_date = format_date(family.marriage)
        individuals_birth = format_date(individual.birthday)

        if((individuals_birth + 14) <= marriage_date):
            print("Error US10: " + individual.id + " marriage before 14")
            return individual.id

    return None

def no_bigamy(family1 = None, family2  = None):

    if(family1 == None or family2 == None):
        return None

    if(family1.husband == family2.husband or family1.wife == family2.wife):
        if(format_date(family2.divorce) > format_date(family1.marriage) or format_date(family1.divorce) > format_date(family2.marriage)):
            print("US11:  bigamy " +family1.id + " and " + family2.id)
            return (family1, family2)
    return None

def Parents_not_too_old(family = None):
    if(family ==None):
        return None
    wife = get_indiv(family.wife)
    husband = get_indiv(family.husband)
    child = get_indiv(family.children)

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

def user_stories(conn):

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    familes = cur.fetchall()

    for family in familes:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = Family(family[0], family[1], family[2],family[3],family[4],family[5],)



        #loop through each individual in the family
        for indiv in family[3:5]:

            if indiv != None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()

                indiv_obj = Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

                birth_before_parents_marriage(indiv_obj, fam_obj)



