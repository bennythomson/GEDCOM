import datetime


# Initialize variables for the individual dnd family fields (pull up fields)
# Individual's Attributes: ID, Name, sex, birth, aliveBoolean, death, child, spouse
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


# Family Attributes: ID, Marriage date, divorce date, husband ID, wife ID, children
class Family:
    def __init__(self, id, marriage, divorce, husband, wife, children):
        self.id = id
        self.marriage = marriage
        self.divorce = divorce
        self.husband = husband
        self.wife = wife
        self.children = children


# Extract the method which formats the date appropriately
def reformat_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def birth_after_marriage(individual=None, family=None):

    if individual is not None and family is not None:
        if individual.birthday is None or family.marriage is None:
            return None

        marriage_date = reformat_date(family.marriage)
        birth_date = reformat_date(individual.birthday)

        if birth_date >= marriage_date:

            print("Error US02: " + individual.id + " marriage before birth")
            return individual.id

    return None


def birth_before_death(individual=None):
    if individual is not None:
        if individual.birthday is None or individual.death is None:
            return None
    birth_date = reformat_date(individual.birthday)
    death_date = reformat_date(individual.death)

    if birth_date >= death_date:

        print("Error US03: " + individual.id + "death before birth")
        return individual.id

    return None


def paul_user_stories(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    families = cur.fetchall()

    for family in families:

        for indiv in family[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv), ))
                indiv_result = new_cur.fetchall()

                birth_after_marriage(indiv_result[0], family)
                birth_before_death(indiv_result[0])
