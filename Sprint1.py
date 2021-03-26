import classes
import datetime
from datetime import date


def format_date(date_str):
    #takes in a string repreenting a date in Y-m-d format and returns a datetime object
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def marriage_after_death(individual=None, family=None):
    #dont fear the reaper....

    '''This method returns the ID of the individual if their marriage date occurs
    after their death date'''
    if(individual != None and family != None):
        #check if the death date or marriage date are none
        if(individual.death == None or family.marriage == None):
            return None


        #print("death " + individual.death)
        #print(" ind: " + individual)
        #print("fam : " + family)

        marriage_date = format_date(family.marriage)
        individuals_death = format_date(individual.death)

        if(individuals_death <= marriage_date):
            print("Error US05: " + individual.id + " marriage after death")
            return individual.id

    return None

def marriage_before_divorce(family=None):

    if(family.marriage == None or family.divorce == None):
        return None

    marriage_date = format_date(family.marriage)
    divorce_date = format_date(family.divorce)

    if(marriage_date >= divorce_date):
        print("Error US04: " + family.id + " divorce date after marriage")
        return family.id

    return None



def birth_after_marriage(individual=None, family=None):

    if individual is not None and family is not None:
        if individual.birthday is None or family.marriage is None:
            return None

        marriage_date = format_date(family.marriage)
        birth_date = format_date(individual.birthday)

        if birth_date >= marriage_date:

            print("Error US02: " + individual.id + " marriage before birth")
            return individual.id

    return None


def birth_before_death(individual=None):
    if individual is not None:
        if individual.birthday is None or individual.death is None:
            return None
    birth_date = format_date(individual.birthday)
    death_date = format_date(individual.death)

    if birth_date >= death_date:

        print("Error US03: " + individual.id + "death before birth")
        return individual.id

    return None

def divorce_after_death(individual=None, family=None):
    '''returns an error if an individual was divorced after they died'''
    # for those who don't have empty information
    if individual and family is not None:
        if individual.death is None or family.divorce is None:
            return None


        divorce_date = format_date(family.divorce)
        individuals_death = format_date(individual.death)

        # check if divorce date is greater than death date, print the error, return the individual
        if divorce_date > individuals_death:
            print("Error US06: ", individual[0], " got divorced after death")
            return individual.id

    return None

def less_than_150(individual=None):
    '''returns the individual's ID if they are older than 150'''
    if individual.birthday is not None:
        birth_date = format_date(individual.birthday)

    if individual.death is not None:
        death_date = format_date(individual.death)
        age_1 = int((death_date - birth_date).days / 365)
        # print(age_1)
        if age_1 >= 150:
            print("Error US07: " + individual.id + " is older than 150 years old")
            return individual[0]

    if individual.birthday is not None:
        age_2 = int((date.today() - birth_date).days / 365)
        if age_2 >= 150:
            print("Error US07: " + individual.id + " is older than 150 years old")
            return individual.id

    return None



def user_stories(conn):

    '''executes all of the user stories contained in this module'''

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    familes = cur.fetchall()

    for family in familes:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = classes.Family(family[0], family[1], family[2],family[3],family[4],family[5],)

        marriage_before_divorce(fam_obj)


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

                marriage_after_death(indiv_obj, fam_obj)
                birth_after_marriage(indiv_obj, fam_obj)
                divorce_after_death(indiv_obj, fam_obj)
                birth_before_death(indiv_obj)
                less_than_150(indiv_obj)
