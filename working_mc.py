import datetime
from datetime import date

# How to fix Bad Smell #1: create different objects to identify the columns
class Indiv:

    def __init__(self, id, name, sex, birthday, alive, death, children, spouse):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.alive = alive
        self.death = death
        self.children = children
        self.spouse = spouse

class Fam:
    def __init__(self, id, marriage, divorce, husband, wife, children):
        self.id = id
        self.marriage = marriage
        self.divorce = divorce
        self.husband = husband
        self.wife = wife
        self.children = children

# How to fix bad smell 2: create a variable for formatting time to reference
def formatting(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def divorce_after_death(individual=None, family=None):
    # for those who don't have empty information
    if individual is not None and family is not None:

        # skip those who have no death date or divorce date
        # Bad Smell #1: Can improve gathering data from the data base
        if individual.death is None or family.divorce is None:
            return None

        # set the columns to check from the two data tables and convert dates for manipulation
        divorce_date = formatting(family.marriage)
        individuals_death = formatting(individual.death)

        # check if divorce date is greater than death date, print the error, return the individual
        if divorce_date > individuals_death:
            print("Error US06: ", individual.id, individual.name, "got divorced after death")
            return individual.id

    return None

def less_than_150(individual=None):
    if individual is not None:
        birth_date = formatting(individual.birthday)

    if individual.death is not None:
        individuals_death = formatting(individual.death)
        death_date = formatting(individual.death)
        age_1 = int((death_date - birth_date).days / 365)
        # print(age_1)
        if age_1 >= 150:
            print("Error US07: ", individual.id, individual.name, "is older than 150 years old")
            return individual.id

    if individual.death is None:
        age_2 = int((date.today() - birth_date).days / 365)
        if age_2 >= 150:
            print("Error US07: ", individual.id, individual.name, "is older than 150 years old")
            return individual.id

    return None

def mc_user_stories(conn):
    # connect to the data base
    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    # fetch all the rows
    families = cur.fetchall()

    for family in families:

        family_object = Fam(family[0], family[1], family[2], family[3], family[4], family[5])
        divorce_after_death(family_object)

        # manipulate data that for individuals that have information
        for indiv in family[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv),))
                indiv_result = new_cur.fetchall()
                # connect to the defined variable created before
                individual_object = Indiv(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])
                divorce_after_death(individual_object, family_object)

                less_than_150(individual_object)
