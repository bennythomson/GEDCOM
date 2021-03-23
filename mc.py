import datetime
from datetime import date

def divorce_after_death(individual=None, family=None):
    # for those who don't have empty information
    if individual and family is not None:

        # skip those who have no death date or divorce date

        # Bad Smell #1:  There is duplicated code for is None
        if individual[5] is None or family[2] is None:
            return None

        # Bad Smell #2: There is duplicated code for getting the date
        def clean_date(date_str):
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        divorce_date = clean_date(family[2])
        individuals_death = clean_date(individual[5])

        # check if divorce date is greater than death date, print the error, return the individual
        if divorce_date > individuals_death:
            print("Error US06: ", individual[0], " got divorced after death, review Simpson Family")
            return individual[0]


    return None

def less_than_150(individual=None):
    if individual is not None:
        birth_date = datetime.datetime.strptime(individual[3], '%Y-%m-%d').date()

    if individual[5] is not None:
        death_date = datetime.datetime.strptime(individual[5], '%Y-%m-%d').date()
        age_1 = int((death_date - birth_date).days / 365)
        # print(age_1)
        if age_1 >= 150:
            print("Error US07: " + individual[0] + " is older than 150 years old")
            return individual[0]

    if individual[5] is None:
        age_2 = int((date.today() - birth_date).days / 365)
        if age_2 >= 150:
            print("Error US07: " + individual[0] + " is older than 150 years old")
            return individual[0]

    return None






def mc_user_stories(conn):
    # connect to the data base
    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    # fetch all the rows
    families = cur.fetchall()

    for family in families:

        # manipulate data that for individuals that have information
        for indiv in family[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv),))
                indiv_result = new_cur.fetchall()
                # connect to the defined variable created before
                divorce_after_death(indiv_result[0], family)
                less_than_150(indiv_result[0])


